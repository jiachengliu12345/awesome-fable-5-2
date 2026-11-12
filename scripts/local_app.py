#!/usr/bin/env python3
"""Local leaderboard preview with persistent, explicitly local-only test votes."""
import argparse
import copy
import json
import secrets
import sqlite3
import threading
from contextlib import contextmanager
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

import rankings

ROOT = rankings.ROOT
STATIC = ROOT / 'web'


class App:
    def __init__(self, state_dir, snapshot_path=None):
        self.state_dir = Path(state_dir)
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.database = self.state_dir / 'votes.sqlite3'
        self.cache = self.state_dir / 'rankings.json'
        self.data = rankings.read_json(self.cache if self.cache.exists() else (snapshot_path or ROOT / 'data/rankings.json'), {})
        if not self.data.get('works') or not self.data.get('sources'):
            raise ValueError('Run python3 scripts/rankings.py to generate the catalog first')
        self.lock = threading.Lock()
        self.refresh = {'running': False, 'message': '', 'finished_at': None}
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, csrf TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS votes (
                    session_id TEXT NOT NULL REFERENCES sessions(id), work_id TEXT NOT NULL,
                    PRIMARY KEY(session_id, work_id)
                );
            ''')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=10)
        db.execute('PRAGMA foreign_keys = ON')
        try:
            with db:
                yield db
        finally:
            db.close()

    def session(self, candidate):
        with self.connect() as db:
            row = db.execute('SELECT id, csrf FROM sessions WHERE id=?', (candidate,)).fetchone()
            if row:
                return row[0], row[1], False
            identity, csrf = secrets.token_hex(24), secrets.token_hex(24)
            db.execute('INSERT INTO sessions VALUES (?, ?)', (identity, csrf))
            return identity, csrf, True

    def payload(self, identity, csrf):
        with self.lock:
            payload = copy.deepcopy(self.data)
            payload['refresh'] = dict(self.refresh)
        with self.connect() as db:
            totals = dict(db.execute('SELECT work_id, COUNT(*) FROM votes GROUP BY work_id'))
            mine = [row[0] for row in db.execute('SELECT work_id FROM votes WHERE session_id=?', (identity,))]
        payload['local_votes'] = {'totals': totals, 'mine': mine}
        payload['csrf'] = csrf
        return payload

    def vote(self, identity, work_id, voted):
        with self.lock:
            if work_id not in self.data['works']:
                raise ValueError('未找到该作品，请重新加载页面。')
        if type(voted) is not bool:
            raise ValueError('投票状态必须是 true 或 false。')
        with self.connect() as db:
            if voted:
                db.execute('INSERT OR IGNORE INTO votes VALUES (?, ?)', (identity, work_id))
            else:
                db.execute('DELETE FROM votes WHERE session_id=? AND work_id=?', (identity, work_id))

    def start_refresh(self):
        with self.lock:
            if self.refresh['running']:
                return False
            self.refresh = {'running': True, 'message': '正在获取平台数据，通常需要几分钟。', 'finished_at': None}
        threading.Thread(target=self._refresh, daemon=True).start()
        return True

    def _refresh(self):
        try:
            works, sources = rankings.catalog((ROOT / 'README.md').read_text(), (ROOT / 'CODE-AUDIT.md').read_text())
            with self.lock:
                previous = copy.deepcopy(self.data)
            rankings.restore_snapshots(sources, previous['sources'])
            rankings.refresh_sources(sources)
            data = {**previous, 'works': works, 'sources': sources}
            temporary = self.cache.with_suffix('.tmp')
            rankings.write_json(temporary, data)
            temporary.replace(self.cache)
            fresh = sum(s['status'] == 'ok' for s in sources.values())
            failed = sum(s['platform'] != 'YouTube' and s['status'] in {'stale', 'unavailable'} for s in sources.values())
            with self.lock:
                self.data = data
                self.refresh = {'running': False, 'message': f'已更新 {fresh} 个来源；{failed} 个来源未能更新，保留旧值或标为暂无数据。YouTube 保留历史快照。', 'finished_at': rankings.now()}
        except Exception as error:
            with self.lock:
                self.refresh = {'running': False, 'message': f'本次刷新未完成（{type(error).__name__}），仍展示上次保存的数据。', 'finished_at': rankings.now()}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def trusted_host(self):
        port = self.server.server_port
        return self.headers.get('Host') in {f'127.0.0.1:{port}', f'localhost:{port}'}

    def send(self, status, body, content_type='application/json; charset=utf-8', cookie=None):
        if not isinstance(body, bytes):
            body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
        if cookie:
            self.send_header('Set-Cookie', f'fable_local={cookie}; Path=/; HttpOnly; SameSite=Strict; Max-Age=31536000')
        self.end_headers()
        self.wfile.write(body)

    def identify(self):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get('Cookie', ''))
            candidate = cookie['fable_local'].value if 'fable_local' in cookie else ''
        except Exception:
            candidate = ''
        return self.server.app.session(candidate)

    def do_GET(self):
        if not self.trusted_host():
            return self.send(403, {'error': '仅允许本机访问。'})
        path = urlsplit(self.path).path
        if path == '/api/data':
            identity, csrf, new = self.identify()
            return self.send(200, self.server.app.payload(identity, csrf), cookie=identity if new else None)
        files = {'/': ('index.html', 'text/html'), '/app.js': ('app.js', 'text/javascript'), '/style.css': ('style.css', 'text/css')}
        if path not in files:
            return self.send(404, {'error': '页面不存在。'})
        file, kind = files[path]
        return self.send(200, (STATIC / file).read_bytes(), kind + '; charset=utf-8')

    def do_POST(self):
        if not self.trusted_host() or self.headers.get('Origin') != 'http://' + self.headers.get('Host', ''):
            return self.send(403, {'error': '请在本地页面内操作。'})
        identity, csrf, new = self.identify()
        if new or not secrets.compare_digest(self.headers.get('X-CSRF-Token', ''), csrf):
            return self.send(403, {'error': '会话已失效，请重新加载页面。'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length < 0 or length > 4096:
                return self.send(413, {'error': '请求过大。'})
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                raise ValueError('无效的请求。')
            path = urlsplit(self.path).path
            if path == '/api/vote':
                self.server.app.vote(identity, body.get('work_id'), body.get('voted'))
                return self.send(200, self.server.app.payload(identity, csrf))
            if path == '/api/refresh':
                self.server.app.start_refresh()
                return self.send(202, self.server.app.payload(identity, csrf))
            return self.send(404, {'error': '操作不存在。'})
        except (ValueError, TypeError) as error:
            return self.send(400, {'error': str(error)})


def make_server(port, state_dir=None, snapshot_path=None):
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.app = App(state_dir or ROOT / '.local', snapshot_path)
    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--state-dir', type=Path, default=ROOT / '.local')
    args = parser.parse_args()
    server = make_server(args.port, args.state_dir)
    print(f'Local: http://127.0.0.1:{server.server_port}', flush=True)
    print('Local test votes only. Press Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()

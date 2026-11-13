#!/usr/bin/env python3
"""Build separate source-popularity and GitHub reader-vote tables (stdlib only)."""
import argparse
import hashlib
import http.client
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from readme_rankings import render_homepages

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "jiachengliu12345/awesome-code-native-3d"
SECTIONS = {"Games", "Interactive worlds and simulations", "3D films and animations"}
PLATFORMS = ("X", "GitHub", "Bilibili", "YouTube")
ISSUE_MARKER = "<!-- awesome-fable-reader-votes:v1 -->"
BOT = "github-actions[bot]"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def links(text):
    return re.findall(r"\]\((https://[^\s)]+)\)", text)


def source_url(platform, urls):
    for url in urls:
        parsed = urllib.parse.urlparse(url)
        if platform == "X" and parsed.hostname in {"x.com", "twitter.com"}:
            match = re.search(r"/([^/]+)/status/(\d+)", parsed.path)
            if match:
                return "https://x.com/" + match[1] + "/status/" + match[2], match[2]
        if platform == "GitHub" and parsed.hostname == "github.com":
            parts = parsed.path.strip("/").split("/")
            if len(parts) >= 2:
                repo = "/".join(parts[:2])
                return "https://github.com/" + repo, repo.lower()
        if platform == "Bilibili" and parsed.hostname in {"www.bilibili.com", "bilibili.com"}:
            match = re.search(r"/video/(BV[A-Za-z0-9]+)", parsed.path)
            if match:
                return "https://www.bilibili.com/video/" + match[1] + "/", match[1]
        if platform == "YouTube":
            video = None
            if parsed.hostname == "youtu.be":
                video = parsed.path.strip("/")
            elif parsed.hostname in {"www.youtube.com", "youtube.com"}:
                video = urllib.parse.parse_qs(parsed.query).get("v", [None])[0]
            if video:
                return "https://www.youtube.com/watch?v=" + video, video
    return None


def catalog(readme, audit):
    """README remains the source of truth; community discussion rows are excluded."""
    statuses = {}
    for line in audit.splitlines():
        if line.startswith("| "):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                statuses[cells[0]] = cells[1]
    works, sources = {}, {}
    section = ""
    for line in readme.splitlines():
        if line.startswith("## "):
            section = line[3:]
        if section not in SECTIONS or not line.startswith("| **"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 6:
            raise ValueError("Malformed catalog row; expected six columns")
        name = re.match(r"\*\*(.*?)\*\*", cells[0])[1]
        work_id = hashlib.sha256(name.encode()).hexdigest()[:16]
        if work_id in works:
            raise ValueError("Duplicate work: " + name)
        works[work_id] = {
            "name": name, "category": section, "creator": cells[1],
            "url": links(cells[3])[0],
            "audit": statuses.get(name, "Not in code audit / 未纳入代码核验"),
            "sources": [],
        }
        for platform in PLATFORMS:
            # Prefer code links for GitHub, creator/demo links for posts and videos.
            urls = links(cells[4] + " " + cells[3]) if platform == "GitHub" else links(cells[3])
            source = source_url(platform, urls)
            if source is None:
                continue
            url, identity = source
            key = platform + ":" + identity
            works[work_id]["sources"].append(key)
            entry = sources.setdefault(key, {
                "platform": platform, "url": url, "identity": identity,
                "works": [], "metrics": {}, "observed_at": None,
                "status": "unavailable", "scope_notes": [],
            })
            entry["works"].append(work_id)
            pattern = re.escape(platform) + r"([^:<>]*):\s*([^<]+)<br>(\d{4}-\d\d-\d\d \d\d:\d\d) UTC"
            match = re.search(pattern, cells[5])
            if match:
                note = (platform + match[1]).strip()
                if note not in entry["scope_notes"]:
                    entry["scope_notes"].append(note)
                metrics = {}
                for raw, label in re.findall(r"([\d,]+)\s+(views?|likes?|reposts?|replies|comments?|stars?|forks?)\b", match[2]):
                    metric = {"view": "views", "like": "likes", "comment": "comments", "star": "stars", "fork": "forks", "repost": "reposts"}.get(label, label)
                    metrics[metric] = int(raw.replace(",", ""))
                stamp = match[3].replace(" ", "T") + ":00Z"
                if metrics and (not entry["observed_at"] or stamp > entry["observed_at"]):
                    entry.update(metrics=metrics, observed_at=stamp, status="readme_snapshot")
    if not works:
        raise ValueError("No catalog works found")
    return works, sources


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward a GitHub bearer token to a redirect destination.
        raise ValueError("API redirected; review the source URL")


def request_json(url, method="GET", payload=None):
    headers = {"User-Agent": "awesome-fable-rankings/1.0", "Accept": "application/json"}
    if urllib.parse.urlparse(url).hostname == "api.github.com":
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        if os.getenv("GITHUB_TOKEN"):
            headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    data = json.dumps(payload).encode() if payload is not None else None
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.build_opener(NoRedirect).open(req, timeout=20) as response:
        return json.load(response)


def github(path, method="GET", payload=None):
    return request_json("https://api.github.com/repos/" + REPOSITORY + path, method, payload)


def pages(path):
    result = []
    for page in range(1, 101):
        sep = "&" if "?" in path else "?"
        batch = github(path + sep + "per_page=100&page=" + str(page))
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise ValueError("Pagination limit reached; refusing partial vote totals")


def counts(payload, mapping):
    result = {}
    for remote, local in mapping.items():
        value = payload.get(remote)
        if type(value) is int and value >= 0:
            result[local] = value
    return result


def fetch_metrics(source):
    platform, identity = source["platform"], source["identity"]
    if platform == "GitHub":
        body = request_json("https://api.github.com/repos/" + identity)
        return counts(body, {"stargazers_count": "stars", "forks_count": "forks"})
    if platform == "X":
        body = request_json("https://api.fxtwitter.com/status/" + identity)
        if body.get("code") != 200:
            raise ValueError("X reader returned an error")
        return counts(body["tweet"], {"views": "views", "likes": "likes", "retweets": "reposts", "replies": "replies"})
    if platform == "Bilibili":
        body = request_json("https://api.bilibili.com/x/web-interface/view?bvid=" + identity)
        if body.get("code") != 0:
            raise ValueError("Bilibili returned an error")
        return counts(body["data"]["stat"], {"view": "views", "like": "likes", "reply": "comments"})
    raise ValueError("Unsupported automatic provider")


def restore_snapshots(sources, cached):
    for key, entry in sources.items():
        previous = cached.get(key)
        if previous and (previous.get("observed_at") or "") >= (entry["observed_at"] or ""):
            for field in ("metrics", "observed_at", "status", "attempted_at", "error"):
                if field in previous:
                    entry[field] = previous[field]


def refresh_sources(sources):
    def refresh_one(entry):
        if entry["platform"] == "YouTube":
            return 0  # Preserve explicitly dated snapshots; no scraping or hidden API key.
        entry["attempted_at"] = now()
        try:
            metrics = fetch_metrics(entry)
            primary = "stars" if entry["platform"] == "GitHub" else "views"
            if primary not in metrics:
                raise ValueError("Primary metric missing")
            entry.update(metrics=metrics, observed_at=now(), status="ok")
            entry.pop("error", None)
        except (http.client.HTTPException, urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
            entry["status"] = "stale" if entry["metrics"] else "unavailable"
            # No response bodies, credentials, or request headers in stored errors.
            entry["error"] = type(exc).__name__ + (" " + str(exc.code) if isinstance(exc, urllib.error.HTTPError) else "")
            return 1
        time.sleep(0.15)
        return 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        failures = sum(pool.map(refresh_one, sources.values()))
    print(f"Platform refresh: {len(sources)} sources, {failures} failures (previous observations retained)")
    if failures:
        print(f"::warning::{failures} platform sources could not refresh; inspect timestamps and status in POPULARITY.md")


def ballot_marker(work_id):
    return "<!-- awesome-fable-work:" + work_id + " -->"


def is_bot(item):
    return item.get("user", {}).get("login") == BOT and item.get("user", {}).get("type") == "Bot"


def ballot_comments(comments, works):
    result = {}
    for comment in comments:
        if not is_bot(comment):
            continue
        match = re.search(r"<!-- awesome-fable-work:([a-f0-9]{16}) -->", comment.get("body") or "")
        if match and match[1] in works:
            if match[1] in result:
                raise ValueError("Duplicate ballot comment; refusing to split votes")
            result[match[1]] = comment
    return result


def initialize_votes(works):
    if os.getenv("GITHUB_ACTIONS") != "true" or os.getenv("GITHUB_REPOSITORY") != REPOSITORY:
        raise ValueError("Initialize voting only through this repository's manual Actions workflow")
    issues = [i for i in pages("/issues?state=all") if not i.get("pull_request") and is_bot(i) and ISSUE_MARKER in (i.get("body") or "")]
    if len(issues) > 1:
        raise ValueError("Multiple ballot issues; resolve before initialization")
    if issues:
        issue = issues[0]
        if issue["state"] != "open":
            raise ValueError("Voting issue is closed; reopen it before adding works")
    else:
        issue = github("/issues", "POST", {
            "title": "Reader votes / 读者投票 — Fable 5.2 creations",
            "body": ISSUE_MARKER + "\n\nVote with **👍 on a work's bot comment** below. One account can support multiple works; only 👍 counts. Reactions on this issue body or on replies do not count. Remove your 👍 to withdraw a vote.\n\n在对应作品的机器人评论上点 **👍**。每个账号对每个作品计一票，可支持多个作品；其他表情和 Issue 正文上的点赞不计票。取消 👍 即撤票。\n\n[Find a work / 查找作品](https://github.com/" + REPOSITORY + "/blob/main/COMMUNITY-RANKING.md) · [Rules / 规则](https://github.com/" + REPOSITORY + "/blob/main/RANKING-RULES.md)\n\nThe catalog includes pending evidence; popularity is not code verification. / 清单包含待核实作品，票数不代表代码核验结果。",
        })
        time.sleep(2)
    registry = {"repository": REPOSITORY, "issue_number": issue["number"], "issue_url": issue["html_url"]}
    # Write immediately. On an interrupted run, discover existing bot comments by marker.
    write_json(ROOT / "data/voting.json", registry)
    existing = ballot_comments(pages(f"/issues/{issue['number']}/comments"), works)
    for work_id, work in works.items():
        if work_id in existing:
            continue
        body = (ballot_marker(work_id) + "\n\n### " + work["name"] + "\n\n"
                + work["category"] + " · " + work["audit"] + "\n\n"
                + "[Watch / play / 查看作品](" + work["url"] + ")\n\n"
                + "**👍 Vote here / 在本条评论上点赞投票**")
        github(f"/issues/{issue['number']}/comments", "POST", {"body": body})
        time.sleep(2)  # Below GitHub's secondary content-creation limit; POSTs are not retried.
    return registry


def refresh_votes(works, registry, previous):
    if registry.get("repository") != REPOSITORY:
        raise ValueError("Voting registry repository mismatch")
    if not registry.get("issue_number"):
        return {"status": "not_initialized", "observed_at": None, "works": {}}
    try:
        issue = github(f"/issues/{registry['issue_number']}")
        if not is_bot(issue) or ISSUE_MARKER not in (issue.get("body") or "") or issue.get("pull_request"):
            raise ValueError("Voting issue identity mismatch")
        comments = ballot_comments(pages(f"/issues/{registry['issue_number']}/comments"), works)
        results = {}
        for work_id, comment in comments.items():
            value = comment.get("reactions", {}).get("+1")
            if type(value) is not int or value < 0:
                raise ValueError("Missing reaction count; refusing incomplete totals")
            results[work_id] = {"votes": value, "url": comment["html_url"]}
        return {"status": "ok" if issue["state"] == "open" else "closed", "observed_at": now(), "works": results}
    except (http.client.HTTPException, urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
        print("::warning::Reader votes could not refresh; retaining previous observations")
        return {**previous, "status": "stale" if previous.get("observed_at") else "unavailable", "attempted_at": now(), "error": type(exc).__name__}


def escape(text):
    return str(text).replace("|", "&#124;").replace("\n", " ").replace("[", "&#91;").replace("]", "&#93;")


def work_link(work):
    return "[" + escape(work["name"]) + "](" + work["url"] + ")"


def ranked(items, value):
    """Competition ranks, stable alphabetical ordering inside ties (including zero)."""
    ordered = sorted(items, key=lambda item: (-value(item), item[0].casefold()))
    last, rank = None, 0
    for position, item in enumerate(ordered, 1):
        score = value(item)
        if score != last:
            rank = position
        last = score
        yield rank, item


def render(works, sources, registry, votes):
    platform_rows = {}
    intro = ["# Platform popularity / 平台热度榜", "",
             "[Reader votes / 读者投票榜](COMMUNITY-RANKING.md) · [Rules / 规则](RANKING-RULES.md) · [Catalog / 作品清单](README.md)", "",
             "Separate rankings by platform: X / Bilibili / YouTube use views; GitHub uses stars. These are cumulative **source** metrics, not a quality score or a recent-growth chart. Shared posts, videos and repositories appear once. / 各平台分榜，按累计浏览量或 Star 排序；共同来源只计一次，不代表质量或近期增速。", "",
             "Each observation keeps its own timestamp. **stale** means refresh failed and the last observation is retained; **readme_snapshot** is an imported snapshot, not a live fetch. Unknown values are never zero. YouTube snapshots are maintained manually. / 每项保留实际数据时间；stale 为更新失败后保留的旧值，readme_snapshot 为历史快照；未知不计零。YouTube 暂使用人工维护的快照。", ""]
    for platform in PLATFORMS:
        primary = "stars" if platform == "GitHub" else "views"
        entries = [(key, entry) for key, entry in sources.items() if entry["platform"] == platform and primary in entry["metrics"]]
        platform_rows[platform] = list(ranked(entries, lambda item: item[1]["metrics"][primary]))
        intro += ["## " + platform, "", "| Rank / 排名 | Works / 作品 | Source / 来源 | " + primary + " | Other metrics / 其他数据 | Observed (UTC) / 数据时间 | Status / 状态 |", "| --- | --- | --- | ---: | --- | --- | --- |"]
        for rank, (_, entry) in platform_rows[platform]:
            names = " · ".join(work_link(works[i]) for i in entry["works"])
            label = " / ".join(entry["scope_notes"]) or platform
            if len(entry["works"]) > 1:
                label += " · shared / 共用"
            metrics = ", ".join(f"{v:,} {k}" for k, v in entry["metrics"].items() if k != primary) or "—"
            intro.append(f"| {rank} | {names} | [{escape(label)}]({entry['url']}) | {entry['metrics'][primary]:,} | {metrics} | {entry['observed_at']} | {entry['status']} |")
        if not entries:
            intro.append("| — | No measured sources / 暂无可用数据 | — | — | — | — | — |")
        intro.append("")
    missing = [work_link(w) for w in works.values() if not any(sources[k]["metrics"] for k in w["sources"])]
    intro += ["## No measured popularity / 暂无热度数据", "", "These works remain eligible for reader voting. / 仍可参与读者投票。", "", ", ".join(missing) or "None / 无", "",
              "All catalog entries are included; consult the [code audit](CODE-AUDIT.md) before interpreting evidence status. / 榜单覆盖清单作品，代码与模型归因状态请查看核验记录。", ""]
    (ROOT / "POPULARITY.md").write_text("\n".join(intro))
    lines = ["# Reader votes / 读者投票榜", "", "[Platform popularity / 平台热度榜](POPULARITY.md) · [Rules / 规则](RANKING-RULES.md)", "",
             "Click **Vote / 投票**, sign in to GitHub, and add **👍 to that work's bot comment**. Other emoji and reactions on the issue itself do not count. One account can vote for multiple works. / 点击投票链接，在该作品的机器人评论上点 👍；其他表情和 Issue 正文点赞不计票，每个账号可支持多个作品。", "",
             f"Status / 状态: **{votes['status']}** · Observed (UTC) / 数据时间: {votes.get('observed_at') or '—'}", ""]
    if registry.get("issue_url"):
        lines += ["[Voting issue / 投票区](" + registry["issue_url"] + ")", ""]
    else:
        lines += ["Voting is not open yet. After merging, a maintainer runs **Refresh rankings → Run workflow → initialize_votes = true** once. / 投票尚未开放；合并后维护者运行一次工作流并勾选 initialize_votes 即可建立投票区。", ""]
    if votes["status"] in {"stale", "unavailable"}:
        lines += ["Refresh failed; displayed totals are the last successful observation, if available. / 更新失败，保留上次成功统计，未知不计零。", ""]
    lines += ["| Rank / 排名 | Work / 作品 | 👍 | Vote / 投票 | Code audit / 代码核验 |", "| --- | --- | ---: | --- | --- |"]
    known = [(w["name"], i) for i, w in works.items() if i in votes.get("works", {})]
    vote_rows = list(ranked(known, lambda item: votes["works"][item[1]]["votes"]))
    for rank, (_, work_id) in vote_rows:
        w, v = works[work_id], votes["works"][work_id]
        lines.append(f"| {rank} | {work_link(w)} | {v['votes']:,} | [Vote / 投票]({v['url']}) | {escape(w['audit'])} |")
    for work_id, work in works.items():
        if work_id not in votes.get("works", {}):
            lines.append(f"| — | {work_link(work)} | — | Not initialized / 待建立 | {escape(work['audit'])} |")
    lines += ["", "Equal counts share a rank. A dash is unknown, not zero. Bot accounts and coordinated voting are not filtered; this is a community preference poll. / 同票同名次；破折号不是零。未过滤机器人账号或组织投票，本榜仅表达社区偏好。", ""]
    (ROOT / "COMMUNITY-RANKING.md").write_text("\n".join(lines))
    render_homepages(ROOT, works, platform_rows, registry, votes, vote_rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--initialize-votes", action="store_true")
    args = parser.parse_args()
    works, sources = catalog((ROOT / "README.md").read_text(), (ROOT / "CODE-AUDIT.md").read_text())
    previous = read_json(ROOT / "data/rankings.json", {})
    restore_snapshots(sources, previous.get("sources", {}))
    registry = read_json(ROOT / "data/voting.json", {"repository": REPOSITORY, "issue_number": None, "issue_url": None})
    votes = previous.get("votes", {"status": "not_initialized", "observed_at": None, "works": {}})
    if args.initialize_votes:
        registry = initialize_votes(works)
    if args.refresh:
        refresh_sources(sources)
        votes = refresh_votes(works, registry, votes)
    write_json(ROOT / "data/voting.json", registry)
    write_json(ROOT / "data/rankings.json", {"schema_version": 1, "works": works, "sources": sources, "votes": votes})
    render(works, sources, registry, votes)
    print(f"Generated rankings: {len(works)} works, {len(sources)} distinct sources; voting={votes['status']}")


if __name__ == "__main__":
    main()

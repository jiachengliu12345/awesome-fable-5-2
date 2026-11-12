# 本地排行榜

在项目目录运行，无需安装第三方依赖：

```sh
python3 scripts/local_app.py
```

打开 <http://127.0.0.1:8765>。停止服务按 `Ctrl+C`；端口被占用时可加 `--port 8766`。

- **平台热度**：读取已有的真实观测，按 X、GitHub、Bilibili、YouTube 分榜；支持作品／创作者搜索、分类筛选、共用来源去重、观测时间与核验状态展示。未知数据不计零，也不列名次。
- **更新平台数据**：在本机后台刷新 X、GitHub、Bilibili，过程中可以继续浏览；失败保留旧值，YouTube 保留历史快照。若已通过环境变量配置 `GITHUB_TOKEN`，复用它进行 GitHub API 读取；没有 Token 也可以启动并使用历史快照，匿名请求可能限流。
- **读者投票（本地试投）**：每个浏览器会话对每个作品最多一票，重复请求不累加；可以撤回，重启服务后仍保留。多个浏览器的试投会汇总到同一个本地榜，重新加载页面即可读取其他访客的最新票数。同票同名次，无票作品暂不列名次。

本地投票不使用 GitHub 登录，不属于正式 GitHub 投票。更换浏览器或清理 Cookie 可以成为另一位测试访客，因此不可作为公开投票系统。界面始终明确标注“本地试投”。

服务只监听 `127.0.0.1`，不依赖 GitHub Actions。浏览器会话和投票保存在忽略提交的 `.local/votes.sqlite3`，本机刷新的观测保存在 `.local/rankings.json`；不会覆盖正式的 `data/rankings.json`、`data/voting.json` 或向 GitHub 发布评论。需要独立测试空间时使用 `--state-dir /tmp/fable-ranking-test`。

验证：

```sh
python3 -m unittest discover -s tests -v
```

## Local preview (English)

Run `python3 scripts/local_app.py` and open `http://127.0.0.1:8765`. Python 3.9+ and its standard library are sufficient. Browse separate platform rankings, search/filter works, refresh supported sources, and test persistent voting. Local votes are browser-session-based demonstrations, separate from GitHub votes. Runtime data stays in ignored `.local/`; the server binds only to loopback.

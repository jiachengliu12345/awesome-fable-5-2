# Ranking rules / 排名规则

[Platform popularity / 平台热度榜](POPULARITY.md) · [Reader votes / 读者投票榜](COMMUNITY-RANKING.md)

## 两个独立的榜

- **平台热度榜**：X、Bilibili、YouTube 按已收录来源的累计浏览量排名；GitHub 按代码仓库的 Star 排名。各平台分别排名，不把浏览量、点赞、Star 相加。同数值同名次，组内按稳定标识排序。
- **读者投票榜**：一个集中 Issue，每个作品一条机器人评论。登录 GitHub 后，在对应评论上点 **👍** 即投票；一个账号可支持多个作品，每个作品计一次，可取消点赞。其他表情、Issue 正文、读者自行发布的评论不计入。按累计票数降序，同票同名次，再按作品名排序。

这是累计关注度与社区偏好，尚不是“最近一周涨幅”或质量评分。读者榜未过滤机器人账号或组织投票，不承诺一人一票。

## 来源与公平性

- 同一个帖子、视频或 GitHub 仓库只统计一次，关联的多个作品合并显示。合集或比较视频的播放量不归属于单个作品；仓库 Star 不能细分为某个文件的 Star。
- 数据来自 README 的作品区（游戏、交互世界、影片），不包含社区讨论和教程。每个平台默认选取该作品第一条相应来源；GitHub 优先选代码链接。并非搜索全网后的总热度。
- 新作品随 README 自动加入。作品名称哈希作为投票标识；改名会产生新标识，维护者应先迁移旧评论标记以保留票数。删除作品后，旧投票评论保留但不再入榜。
- 包含待核实和未纳入代码核验的作品，核验状态单独显示。是否热门不改变 [CODE-AUDIT.md](CODE-AUDIT.md) 的结论。
- 所有观测保留原始来源链接、指标与 UTC 时间。接口失败保留上次成功观测并标记 `stale`；从未获得的数据为 `unavailable`，不会伪装成零。旧数据和新数据可能来自不同时间，阅读时应比较时间列。
- X 使用第三方 FxTwitter 读取，Bilibili 使用公开视频统计接口，GitHub 使用官方 REST API。第三方接口可能延迟、限流或失效。YouTube 当前保留 README 的人工快照，不自动刷新。

## 启用与维护

1. 合并本 PR，并确保仓库 Issues、GitHub Actions 可用。
2. 打开 **Actions → Refresh rankings → Run workflow**，选择 `main`，勾选 `initialize_votes`。只需首次或添加新作品后运行；重复运行会复用已有 Issue 和评论。首次为所有作品建立评论可能需要数分钟。
3. 运行成功后，`COMMUNITY-RANKING.md` 将提供每个作品的直接投票链接。无需额外服务器、数据库、个人 Token 或第三方账号。
4. 工作流在每天 **09:17、21:17（北京时间）** 定期刷新两榜，支持手动刷新；GitHub 的定时触发可能延迟，公开仓库长期没有活动时也可能停用。README 更新也会触发刷新，但不会自动发布新的投票评论。

`GITHUB_TOKEN` 只发送给 GitHub API；工作流使用 `contents: write` 提交生成文件，使用 `issues: write` 完成手动初始化。PR 检查只读，不初始化投票。若仓库规则限制机器人直接写入主分支，推送步骤会失败，生成文件保存在 `rankings-recovery` artifact，可由维护者通过 PR 纳入。初始化中断后重新运行同一个工作流，它会根据机器人标记发现已建立的评论，不应手动创建第二个投票区。

关闭投票 Issue 后不会自动重开或添加评论；统计会显示 `closed`，关闭 Issue 本身不保证禁止新表情。需要暂停投票时由维护者锁定 Issue 并说明规则。

### 本地检查

```sh
python3 -m unittest discover -s tests -v
python3 scripts/rankings.py            # 离线：使用已保存的观测生成 Markdown
python3 scripts/rankings.py --refresh  # 联网：只读取数据，不发布 Issue 或评论
```

源清单为 `README.md`，结构化观测为 `data/rankings.json`，投票区定位为 `data/voting.json`。不要手工改生成的两个榜单文件。

## English

Platform popularity and reader votes are independent. X, Bilibili and YouTube rank cumulative views; GitHub ranks repository stars. Metrics are never added across platforms. Shared sources appear once, with all associated works. These are source snapshots, not total project reach, quality scores or recent-growth rankings.

Readers vote with 👍 on the designated bot comment for a work. Each GitHub account can support several works, once per work, and withdraw a vote. Other emoji and reactions elsewhere are ignored. Equal counts share a rank. This is an informal preference poll; bot accounts and coordinated voting are not filtered.

After merging, run **Refresh rankings** on `main` with **initialize_votes** checked. Repeat that manual operation when new works are added; existing comments are reused. Refreshes are scheduled for 01:17 and 13:17 UTC and can be delayed by GitHub. No server or personal access token is required. A blocked bot push leaves a recovery artifact rather than bypassing repository rules.

Failed fetches retain the previous observation as `stale`; missing data is never zero. YouTube remains a dated manual snapshot. X uses a third-party reader. Each work's evidence status remains separate from popularity. Work names define voting IDs, so renames need an explicit comment-marker migration to preserve votes.

## API references / 接口依据

- [GitHub reactions](https://docs.github.com/en/rest/reactions/reactions)
- [GitHub repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)
- [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [FxTwitter / FxEmbed](https://github.com/FixTweet/FxTwitter)

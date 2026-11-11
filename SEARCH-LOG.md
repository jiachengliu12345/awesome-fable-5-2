# Search and verification log / 检索与核验记录

The catalog was based on `a0e48ef` after a fast-forward from `908a078`. Search results are leads, not proof of attribution or code access. The final ten searches below were made one at a time, with at least 6.5 seconds between calls; timestamps are UTC on 2026-11-11. They searched indexed public pages, so absence from results is not absence from the platform.

本轮以 `a0e48ef` 为基线，保留了此前远端新增内容。搜索结果只是线索，模型归因和代码可访问性需另行核验。下方最后十轮各自独立搜索，调用之间至少间隔 6.5 秒；时间为 2026-11-11 UTC。网页索引覆盖有限，搜索无结果不代表平台上不存在相关作品。

Before this sequence, searches in the logged-in Bilibili and Xiaohongshu browser sessions found repeated demonstrations of Saltline and Oil paint. A search of itch.io led to **Siege Wing**: the [creator’s page](https://bannerfall.itch.io/siege-wing) identifies Fable 5.2 as used for development, and the [delivered HTML](https://html-classic.itch.zone/html/20442416/index.html?v=1794407879) contains readable game code. Its license was not established. This new eligible work reset the no-result counter.

此前使用已登录浏览器检索 B 站和小红书，发现多条帖子展示的是已收录的 Saltline 和 Oil paint。itch.io 检索发现 **Siege Wing**：[创作者页面](https://bannerfall.itch.io/siege-wing)明确说明 Fable 5.2 参与开发，网页实际交付的 [HTML](https://html-classic.itch.zone/html/20442416/index.html?v=1794407879) 包含可读游戏代码；许可未确认。该作品使连续无结果轮次清零。

| # | UTC | Search / 查询范围 | Outcome / 结果 |
|---|---|---|---|
| 1 | 18:09:28 | Reddit: `"Fable 5.2" "3D" "github" game` | No search results / 无搜索结果 |
| 2 | 18:09:37 | YouTube: `"Fable 5.2" "3D game" source` | No search results / 无搜索结果 |
| 3 | 18:09:48 | itch.io: `"Fable 5.2" "3D" browser` | Siege Wing and Dino Jungle Survival already listed / 命中已收录作品 |
| 4 | 18:09:59 | GitHub: `"Fable 5.2" "three.js" game` | Saltline mirror and existing collection / 命中 Saltline 镜像及已有合集 |
| 5 | 18:10:09 | Bilibili: `"Fable5.2" "源码" 游戏` | Search returned mostly irrelevant indexed results / 搜索结果大多无关 |
| 6 | 18:10:20 | Xiaohongshu: `"Fable 5.2" "源码" 游戏` | No indexed search results / 无索引搜索结果 |
| 7 | 18:10:30 | X: `"Fable 5.2" "play" "source" game` | No indexed search results / 无索引搜索结果 |
| 8 | 18:10:40 | Web: `"Fable 5.2" "webgl" game playable` | Existing Kevin Ngo games and collections / 命中已收录作品及合集 |
| 9 | 18:10:52 | Web: `"Fable 5.2" game "github.io"` | Sumi lead is described as a 2D platformer; VELA BAY already listed / Sumi 为 2D 平台游戏线索；VELA BAY 已收录 |
| 10 | 18:11:02 | Web: `"Fable 5.2" interactive 3d source code game` | No additional qualifying work verified / 未核实到新增合格作品 |

Ten consecutive completed searches yielded no newly verified qualifying work; phase one stopped at this working threshold, not because the web or any platform was exhausted. Full candidate verification and existing-entry audit remain subject to the access limits described below.

连续十轮完成检索后，没有核实到新的合格作品，因此按工作停止条件结束第一阶段；这不代表已穷尽各平台。候选及已有条目的核验仍受下述访问限制影响。

Earlier parallel investigation bundled multiple searches or page opens in single calls, so the five-second spacing between individual operations could not be established. Those batches were **not** counted toward the ten rounds. Their leads were used only where separately checked. The Claude Saltline artifact remained on a loading screen in the browser; readable source was not independently confirmed. Some Evals asset requests returned 403 in a separate audit, while other requests to the service succeeded; affected entries are marked for rechecking. Several entries have code but need stronger evidence connecting the specific work to the named model.

此前部分并行调查在一次调用中合并了多项搜索或页面访问，无法确认每项操作之间有五秒间隔；这些批次**未计入**上述十轮。线索只有另行核实后才使用。Saltline 的 Claude artifact 在浏览器中持续加载，未能独立确认源码可读。另一次核验中部分 Evals 作品文件返回 403，同一服务的其他请求则成功；相关条目已标待复核。部分作品虽有代码，但特定作品与模型的对应关系仍需更强证据。

At this checkpoint the two READMEs each contain 139 work rows and 85 entries in the code index, including Siege Wing. Twelve index entries are explicitly marked as needing model attribution or code-access verification; the remaining 73 have not all been independently rechecked against every acceptance condition by the integrator, so 73 is an upper bound after these exclusions, not a verified final count. The latest remote additions before this work are not counted as additions made in this session. One work was added in this session.

本次检查时，两份 README 各有 139 条作品记录、85 条代码索引（包括 Siege Wing）。其中 12 条明确标注模型归因或代码访问待核实；其余 73 条尚未由整合者逐一独立复核全部验收条件，因此 73 只是扣除已标疑点后的上限，不是已核实的最终合格数。本次工作之前远端新增的作品不计为本轮新增；本轮新增 1 件作品。

## Resource discovery / 资源检索（2026-11-12）

The follow-up covered Reddit, X, GitHub, creator tutorials, asset libraries and official tool documentation. Parallel workers returned candidate sources for the coordinator to check and integrate. Search results are discovery leads; linked skills and tools were not installed or independently run. An X search found the already-listed Sunny Valley Studio post; the X original and its linked video remained inaccessible during direct checking. One GitHub candidate (`Olioli4/blender2three-skills`) returned 404 and was not added. Search timings from early parallel work were not all recorded precisely, so they are not used to reconstruct the final five-round sequence.

后续检索覆盖 Reddit、X、GitHub、创作者教程、资产库和官方工具文档。并行检索返回线索后，由整合者核查并加入清单；我们没有安装或独立运行所收录的 Skills 与工具。X 搜索命中已列出的 Sunny Valley Studio 帖子，直接访问原帖及关联视频仍受限。GitHub 候选 `Olioli4/blender2three-skills` 返回 404，未收录。早期并行工作的逐次时间未完全记录，因此未用于重建最终五轮计数。

After the newly identified Meshy DCC Core resource, the following searches found no additional resource with a distinct, verifiable contribution. Times are UTC on 2026-11-11, recorded by the search worker:

找到 Meshy DCC Core 后，以下检索未发现具有明确、可核实独立价值的新增资源。时间为 2026-11-11 UTC，由检索任务记录：

| Completion / 时间 | Search scope / 查询 | Outcome / 结果 |
| --- | --- | --- |
| 18:52:05 | `AI coding agent interactive world code animation video tutorial Godot Blender Unity Three.js resource guide` | Repeated existing categories / 已有类别重复 |
| 18:52:26 | `AI agent Blender video 3D model scene skill first-party documentation game asset MCP agent coding tutorial` | Repeated Blender/Scenario resources / Blender、Scenario 类资源重复 |
| 18:52:52 | `AI code-driven video tools skill game worlds 3D worlds assets agent tutorials GitHub 2026` | Repeated code-video and skill collections / 代码影片与技能合集重复 |
| 18:53:20 | `3D game asset generation agent skill official Meshy Tripo Blender Unity Godot tutorial recent` | Product tutorials did not show distinct workflow value beyond collected entries / 产品教程未显示超出现有条目的独立工作流价值 |
| 18:54:58 | `site:docs.meshy.ai AI agent game development 3D scene workflow tutorial` | Repeated Meshy resources / 与已有 Meshy 资料重复 |

An intervening search (`AI coding agent skill official game engine 3D creation interactive worlds code video tutorial tools assets`) returned a truncated result and was not counted. Search stopped after five completed no-new-resource rounds; the result reflects the chosen queries and relevance threshold, not an exhaustive inventory. Earlier findings include the already-integrated Scenario Skills; candidates that overlap existing tools without a demonstrated distinct use are retained as leads, not separate entries.

中间另有一次搜索输出被截断，未计入有效轮次。连续五轮完成检索未找到新资源后停止；这只反映所选查询和收录标准，并非穷尽所有资源。先前发现包括已加入的 Scenario Skills；对已收工具没有显示独立用途的重叠候选只作线索，不另列条目。

## Final code audit / 最终代码核验（2026-11-12）

The later work-by-work audit supersedes the earlier checkpoint above: 48 verified, 34 pending and 3 outside scope among 85 code-index entries. See [CODE-AUDIT.md](CODE-AUDIT.md) for statuses, evidence links and limits. The full catalog has 139 work rows; Siege Wing was the one addition in this session. The 8 Evals outputs were rechecked successfully after the earlier intermittent 403 responses.

后续逐项核验取代上方早期检查点：85 条代码索引中，48 条已核实、34 条待核实、3 条不在范围内。状态、证据链接及限制见[代码核验表](CODE-AUDIT.md)。完整清单有 139 条作品，本轮新增 Siege Wing 1 件。早先部分 Evals 文件曾返回 403，后续 8 个输出已重新核验成功。

## Follow-up code review / 代码复核（2026-11-12）

Revisited all 34 entries pending at the previous checkpoint. Fifteen were promoted after matching source, work and model evidence, resulting in 63 verified, 19 pending and 3 outside scope among 85 code-index entries. This is a conservative verified minimum. See the [audit](CODE-AUDIT.md) for source-specific limitations, including inaccessible X originals and the 11 supplied MiaAI files. No additional work was added to the catalog in this follow-up.

复查上一检查点的全部 34 条待核条目后，15 条因作品、源码和模型证据能够对应而转为已核实；85 条代码索引现为 63 条已核实、19 条待核、3 条不在范围内。该数量是保守下限。具体证据与限制见[核验表](CODE-AUDIT.md)，包括 X 原站无法访问和 11 个来源待查的 MiaAI 文件。本次复核未新增作品条目。

# Code asset search / 代码资产检索

12 November 2026 (UTC+8). The search looked for editable procedural 3D object code, reusable asset generators and closely related research corpora. Sand3D and other existing entries were checked for duplication. Three parallel Luna workers researched GitHub projects, Hugging Face datasets and other official sites; overlapping discovery requests were treated as leads, not counted toward the stopping sequence. We checked project READMEs, license files and dataset cards, without running the generators or downloading the corpora.

2026 年 11 月 12 日（UTC+8）。本次检索范围为可编辑的程序化 3D 对象代码、可复用资产生成器及相关研究数据集，并对照既有 Sand3D 等条目去重。三个 Luna 子任务分别检索 GitHub 项目、Hugging Face 数据集和其他官方网站；可能重叠的并发发现查询只作为线索，不计入停止轮次。我们核对了项目说明、许可文件及数据卡，没有运行生成器或下载数据集。

Discovery covered queries such as `procedural 3D asset library Blender Python`, `Three.js procedural asset generator`, `OpenSCAD parametric parts`, and `site:huggingface.co/datasets 3D code dataset procedural generation`. General 3D model stores were not counted as code-asset libraries without evidence of editable source. Patch Toolbox was a lead from Reddit; the web reader could not inspect its asset page, and its specific systems and their licenses were not independently established, so it was not added as a verified code library. JSCAD documentation returned 504 in the main web check and was not added. Failed or restricted access was not counted as a no-result search.

发现阶段检索了 `procedural 3D asset library Blender Python`、`Three.js procedural asset generator`、`OpenSCAD parametric parts`、`site:huggingface.co/datasets 3D code dataset procedural generation` 等范围。普通 3D 模型商店在没有可编辑源码证据时不计作代码资产库。Reddit 上的 Patch Toolbox 是一条线索；网页读取工具未能检查其资产页，具体系统及各自许可尚未独立确认，因此未作为已核实代码库收录。JSCAD 文档在主核验中返回 504，也未收录。报错或访问受限不计作无结果检索。

The last accepted increment was FoldNet, with the generator's code license explicitly unconfirmed. After that, five web-index searches completed in order around 19:10–19:12 UTC+8 without another qualified addition. Results reflect the accessible index, not comprehensive coverage of platform-native search. The X and Xiaohongshu indexes were sparse; no login, CAPTCHA or access limit was bypassed.

最后一个合格增量是 FoldNet，文档明确标注其生成代码许可未确认。此后约 19:10–19:12（UTC+8）依次完成以下五次网络索引检索，没有新的合格增量，触发本轮停止条件。索引结果不代表平台站内搜索已完整覆盖；X 和小红书索引较稀疏，未绕过登录、验证码或访问限制。

| Round | Platform and query / 平台与查询 | Outcome / 结果 |
| --- | --- | --- |
| 1 | X index: `"procedural 3d assets" "source code" Blender dataset` | No indexed results / 索引无结果 |
| 2 | YouTube index: `"procedural 3d" "asset library" "source code" Blender` | No indexed results / 索引无结果 |
| 3 | Xiaohongshu index: `3D 程序化 建模 资产库 代码 开源` | Irrelevant platform documents and job listings / 平台说明及招聘，未见合格资产库 |
| 4 | Bilibili index: `"程序化" "3D" "开源" "资产" Blender Python 资源库` | Tutorials and download listings; no newly verified code-asset library with clear source and terms / 教程与下载合集，未找到新核实的代码资产库及明确条款 |
| 5 | DEV index: `"procedural 3d" "asset library" "open source" code game` | No indexed results / 索引无结果 |

## Continued search / 后续检索 — 2026-11-12

Parallel Luna workers searched GitHub, Hugging Face, Reddit and official sites for editable procedural 3D code, node assets and scene data. This pass added ten distinct resources to the bilingual catalog and linked an expanded corpus under the existing 3DCodeBench entry rather than counting its benchmark twice. Kiln and img2threejs already appear in the wider resource guide. Code, generated outputs, node graphs, paid assets and dataset rights are distinguished in the catalog. We inspected public descriptions and licenses; we did not install software, log in, download the datasets or run the assets.

本轮由 Luna 并行检索 GitHub、Hugging Face、Reddit 和项目官网，范围包括可编辑的程序化 3D 代码、节点资产与场景数据。双语目录新增 10 项不同资源；3DCodeBench 的扩展语料并入原条目，未将同一评测集重复计数。Kiln 和 img2threejs 已在资源指南中。目录分别说明代码、生成结果、节点图、付费资产和数据集的许可；本次仅核对公开说明及许可，没有安装软件、登录、下载数据集或运行资产。

Discovery queries included `procedural 3D assets generator Blender geometry nodes`, `Three.js procedural model generator export glb`, `site:reddit.com/r/threejs procedural model library generator source code models`, and `site:huggingface.co/datasets procedural 3D scene Blender Python environment dataset code generation scenes`. Polyspoon's cited GitHub repository returned 404, so source and license remain unconfirmed. Patch Toolbox's asset browser returned an internal error; the publisher describes a mixed catalog with per-item licenses, but individual source access and rights were not verified. IDEAL-Scenes' file listing could not be inspected. These restricted checks are leads, not completed no-result rounds.

发现阶段的查询包括 `procedural 3D assets generator Blender geometry nodes`、`Three.js procedural model generator export glb`、`site:reddit.com/r/threejs procedural model library generator source code models` 和 `site:huggingface.co/datasets procedural 3D scene Blender Python environment dataset code generation scenes`。Polyspoon 所引用的 GitHub 仓库返回 404，源码和许可待确认；Patch Toolbox 的素材浏览页返回内部错误，发布方描述其为逐项授权的混合素材目录，但具体源码入口及权利未核实；IDEAL-Scenes 文件列表未能检查。这些受限检查只作为线索，不计入无结果轮次。

After accepting the last discovery, five sequential web-index searches around 19:23–19:25 UTC+8 produced no additional qualified resource; the stop condition was met. These are searches of the available web index, not exhaustive platform-native coverage. X and YouTube results were sparse; Bilibili included tutorials and listings whose asset sources and permissions were not established. No login, CAPTCHA or access restriction was bypassed.

接纳最后一项发现后，约 19:23–19:25（UTC+8）按顺序完成以下五次网络索引检索，没有新的合格资源，达到停止条件。这些是可用网页索引检索，并非各平台站内的全面覆盖；X 和 YouTube 索引结果稀疏，B 站结果包含未能确认素材来源与许可的教程和合集。未绕过登录、验证码或访问限制。

| Round | Platform and query / 平台与查询 | Outcome / 结果 |
| --- | --- | --- |
| 1 | Reddit index: `site:reddit.com/r/proceduralgeneration "procedural" "source" "assets" 3d` | Existing Infinigen and project demonstrations; city pipeline post did not provide a source link / 既有 Infinigen 与项目展示；城市生成帖未提供源码链接 |
| 2 | Hugging Face index: `site:huggingface.co/datasets "3d" "procedural" "code" "Blender" benchmark` | Existing 3DCodeBench, its linked expanded corpus and 3DCodeVerse / 既有 3DCodeBench、已并入的扩展语料和 3DCodeVerse |
| 3 | X index: `site:x.com "procedural" "3d" "asset" generator github` | Simulation announcement; no newly verified editable asset library / 仿真项目介绍，未找到新核实的可编辑素材库 |
| 4 | Bilibili index: `site:bilibili.com 程序化 资产库 建模 源码 blender 生成器` | Tutorials and listings without a verified new library and terms / 教程及合集，未核实新的素材库及其条款 |
| 5 | YouTube index: `site:youtube.com/watch "procedural" "asset library" "source" blender` | No indexed results / 索引无结果 |

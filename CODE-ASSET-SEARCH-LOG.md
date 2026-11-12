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

## Commercial-friendly open-source search / 开源及可商用资源续查 — 2026-11-12

Four Luna workers searched GitHub, Hugging Face, Reddit and project websites for editable procedural 3D programs, node assets and related datasets. We checked the original project descriptions and stated licenses and compared project identities against this catalog and the general resource guide. Software licenses, asset licenses, third-party components and generated-output rights are described separately; GPL/MPL obligations and early-stage limitations are retained. We did not independently install, generate or render the assets. Resources are general-purpose and are not claims of Fable 5.2 authorship.

四个 Luna 子任务检索 GitHub、Hugging Face、Reddit 及项目官网，寻找可编辑的程序化 3D 程序、节点资产和相关数据集。我们核对项目原始说明及其声明的许可，并对照本目录和通用资源指南去重。文档分别记录软件、素材、第三方组件及生成结果的权利，并保留 GPL/MPL 分发义务和项目早期状态等限制；未独立安装、生成或渲染资产。这些是通用资源，不代表使用了 Fable 5.2 制作。

Discovery queries included `Blender Geometry Nodes assets license CC0 procedural asset library`, `site:reddit.com Godot procedural tree generator github license`, `site:huggingface.co/datasets procedural 3D scene Blender Python environment dataset code generation scenes`, and `procedural 3D asset generator Blender license MIT geometry nodes assets`. Wadi was excluded from commercial-asset recommendations because its repository distinguishes the app license from reusable house designs. CAD-Coder's Apache label did not establish rights to its upstream Text2CAD source, which has non-commercial restrictions; it was not added as a verified commercial asset dataset. General asset stores without editable procedural sources were excluded from this pass.

发现阶段的查询包括 `Blender Geometry Nodes assets license CC0 procedural asset library`、`site:reddit.com Godot procedural tree generator github license`、`site:huggingface.co/datasets procedural 3D scene Blender Python environment dataset code generation scenes` 和 `procedural 3D asset generator Blender license MIT geometry nodes assets`。Wadi 的仓库区分应用代码许可与房屋设计的复用许可，因此未作为商用资产推荐；CAD-Coder 的 Apache 标签不能消除其上游 Text2CAD 的非商业限制，未列为已核实的可商用资产数据集。本轮不将缺少可编辑程序化源码的普通素材商店计入。

Additional leads included Shoals fish-school nodes (the addon download and its own code license were not confirmed) and a CC0 barbed-wire `.blend` shared in a creator post (the file itself was not inspected). Neither was presented as a verified reusable code library. A scientific Blender asset library, CGFigures, was added with its CC0 declaration and the unchecked download clearly noted.

其他线索包括 Shoals 鱼群节点插件（未确认插件下载入口及其代码许可）和创作者帖子中声明为 CC0 的刺丝网 `.blend` 文件（未检查文件本身）；均未作为已核实的可复用代码库收录。另新增科学可视化 Blender 素材库 CGFigures，并明确标注其 CC0 声明和下载内容未独立检查。

After the final accepted increment, five completed web-index searches around 21:14–21:15 UTC+8 returned no additional qualified resource, meeting the stopping condition. These searches reflect indexed public pages rather than exhaustive platform-native coverage; sparse X/YouTube results and inaccessible individual asset pages limit coverage. Failed page fetches and unverified leads were not themselves treated as successful searches. No login, CAPTCHA or platform limit was bypassed.

最后一个合格增量之后，约 21:14–21:15（UTC+8）依次完成五次网页索引检索，未发现新的合格资源，达到停止条件。这些是公开网页索引，而非平台站内的完整覆盖；X、YouTube 结果稀疏，部分素材页面无法访问。页面读取失败和未核实线索本身不计为成功检索；未绕过登录、验证码或平台限制。

| Round | Platform and query / 平台与查询 | Outcome / 结果 |
| --- | --- | --- |
| 1 | X index: `site:x.com "procedural 3d" "asset library" "open source"` | No indexed results / 索引无结果 |
| 2 | Bilibili index: `site:bilibili.com "程序化" "资产库" "开源" Blender` | Tutorials and listings without a newly verified license and source / 教程及素材清单，未核实新的源码与许可 |
| 3 | Hugging Face index: `site:huggingface.co/datasets "Blender" "procedural" "code" "cc0"` | Material images and unrelated dataset indexes, not newly verified editable procedural code / 材质图片及无关数据索引，未核实新的可编辑程序化代码 |
| 4 | YouTube index: `site:youtube.com/watch "procedural" "3d asset library" "open source"` | No indexed results / 索引无结果 |
| 5 | Reddit index: `site:reddit.com/r/proceduralgeneration "open source" "asset library" blender` | Previously assessed Patch catalog and already-listed generators; no new qualified resource / 已核查的 Patch 目录和已收录生成器，未找到新合格资源 |

## Continued tools and asset search / 工具与资产续查 — 2026-11-12

The user supplied Astrocade MCP, and three Luna workers searched for related game-publishing tools and editable procedural 3D assets. This pass added Astrocade, Origin MCP and PlayDrop MCP to the general resource guide, plus five asset or research entries to this catalog. Hosted services are not treated as open-source asset libraries. We checked provider pages, dataset cards and repository licenses; we did not sign in, install, download or run the tools. The Astrocade terms inspected state personal, non-commercial use; the documentation notes separate creator-program agreements may apply.

用户提供 Astrocade MCP 后，三个 Luna 子任务继续检索游戏发布工具和可编辑程序化 3D 资产。本轮在通用资源指南中加入 Astrocade、Origin MCP 和 PlayDrop MCP，并在本目录新增五项资产或研究资源。托管平台不按开源素材库处理。我们核对了服务方页面、数据卡和仓库许可；没有登录、安装、下载或运行这些工具。所查 Astrocade 服务条款写明个人非商业用途，文档也提示可能另有创作者计划协议。

Discovery queries included `AI game creation platform MCP publish game official`, `site:github.com procedural 3D model generator Blender "CC0" asset library`, and `site:reddit.com "procedural" "3d assets" "code" "MIT" generator`. Patch Toolbox remained a previously recorded lead: its asset browser could not be inspected, so its individual systems and licenses were not confirmed. An image-to-3D add-on had no identified license and did not establish editable procedural source. A delegated follow-up failed; the French town nodes and CCORE dataset were subsequently checked against their original repository and dataset card. No failed operation was counted as a no-result search.

发现阶段的查询包括 `AI game creation platform MCP publish game official`、`site:github.com procedural 3D model generator Blender "CC0" asset library` 和 `site:reddit.com "procedural" "3d assets" "code" "MIT" generator`。Patch Toolbox 仍是此前记录的线索：素材浏览页无法检查，具体系统及逐项许可未确认。一个图生 3D 插件未找到许可，也未确认提供可编辑的程序化源码。一次委派复查失败后，我们另行查阅法式小镇节点的原始仓库与 CCORE 数据卡。失败操作未计入无结果轮次。

After the last accepted addition, five sequential web-index searches around 21:34–21:35 UTC+8 found no further qualified increment, meeting the stopping condition. Results are limited to accessible indexed pages, not comprehensive platform-native searches; sparse X and YouTube results and inaccessible individual sources remain limitations. No login or platform restriction was bypassed.

接纳最后一个增量后，约 21:34–21:35（UTC+8）依次完成五次网页索引检索，未找到新的合格增量，达到停止条件。结果限于可访问的公开索引，并非平台站内全面检索；X、YouTube 索引稀疏，部分来源无法访问。未绕过登录或平台限制。

| Round | Platform and query / 平台与查询 | Outcome / 结果 |
| --- | --- | --- |
| 1 | X index: `site:x.com "procedural 3d" "asset library" "open source"` | No indexed results / 索引无结果 |
| 2 | Bilibili index: `site:bilibili.com "程序化" "资产库" "开源" Blender` | Tutorials and listings without a newly verified library and terms / 教程和合集，未核实新的素材库及条款 |
| 3 | Hugging Face index: `site:huggingface.co/datasets "Blender" "procedural" "code" "cc0"` | Material images and unrelated dataset indexes, no new verified procedural source / 材质图片与数据索引，未核实新的程序化源码 |
| 4 | YouTube index: `site:youtube.com/watch "procedural" "3d asset library" "open source"` | No indexed results / 索引无结果 |
| 5 | Reddit index: `site:reddit.com/r/proceduralgeneration "open source" "asset library" blender` | Previously assessed Patch lead and existing resources; no new qualified entry / 既有 Patch 线索和已收录资源，无新合格条目 |

## Open-source assets and skills / 开源资产与技能续查 — 2026-11-12

Four Luna workers searched for editable procedural 3D assets, generators, skills and relevant Reddit/X leads. This pass added five assets or tools to the code-asset catalog and one Skill to the dedicated skills document. Repositories, licensing notices and the Skill entry point were checked; we did not install or run the projects. GPL obligations, bundled texture rights and uncertain output rights are identified per entry.

四个 Luna 子任务分别检索可编辑程序化 3D 资产、生成器、技能及 Reddit/X 线索。本轮在代码资产目录新增五项资产或工具，并在技能专题文档新增一项 Skill。已核查项目仓库、许可说明及技能入口；没有安装或运行项目。各条目分别说明 GPL 义务、附带纹理权利和未确认的生成结果许可。

Discovery queries included `GitHub procedural 3D asset generator open source MIT Blender procedural models`, `site:github.com "SKILL.md" procedural 3D Blender game assets agent skill`, and `GitHub skill Blender procedural modeling game assets SKILL.md`. Kiln and Procedura were excluded as existing entries after a broader repository check. Space Robotics Bench Assets was retained only as a lead: its authors label their assets and pipeline outputs CC0, but the code license and third-party assets require separate confirmation. Failed or restricted checks were not counted as no-result rounds.

发现阶段的查询包括 `GitHub procedural 3D asset generator open source MIT Blender procedural models`、`site:github.com "SKILL.md" procedural 3D Blender game assets agent skill` 和 `GitHub skill Blender procedural modeling game assets SKILL.md`。经扩大范围查重，Kiln 和 Procedura 均已收录。Space Robotics Bench Assets 暂留作线索：作者将自制素材与流水线输出标为 CC0，但代码许可及第三方资产仍需分别核对。失败或受限操作不计入无结果轮次。

After the final accepted increment, five sequential web-index searches around 23:56–23:57 UTC+8 returned no further qualified resource. The stop condition was met. The searches below were actually rerun, including queries used in an earlier pass; they cover public indexes, not exhaustive platform-native search. X and YouTube were sparse; no login, CAPTCHA or access restriction was bypassed.

最后一个合格增量之后，约 23:56–23:57（UTC+8）依次完成五次网页索引检索，未发现新的合格资源，达到停止条件。以下查询均已实际重新执行，其中部分与此前一轮相同；覆盖范围是公开索引，并非平台站内全面检索。X 和 YouTube 索引结果稀疏，未绕过登录、验证码或访问限制。

| Round | Platform and query / 平台与查询 | Outcome / 结果 |
| --- | --- | --- |
| 1 | X index: `site:x.com "procedural 3d" "asset library" "open source"` | No indexed results / 索引无结果 |
| 2 | Bilibili index: `site:bilibili.com "程序化" "资产库" "开源" Blender` | Tutorials and listings without newly verified source and terms / 教程及合集，未核实新的源码与条款 |
| 3 | Hugging Face index: `site:huggingface.co/datasets "Blender" "procedural" "code" "cc0"` | Material images and indexes; no newly verified editable procedural source / 材质图片与索引，未核实新的可编辑程序化源码 |
| 4 | YouTube index: `site:youtube.com/watch "procedural" "3d asset library" "open source"` | No indexed results / 索引无结果 |
| 5 | Reddit index: `site:reddit.com/r/proceduralgeneration "open source" "asset library" blender` | Previously assessed Patch lead and existing resources; no qualified addition / 既有 Patch 线索及已收录资源，无新合格增量 |

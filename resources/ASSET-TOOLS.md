# Asset libraries and production tools / 资产库与制作工具

[Resource directory / 资源目录](../RESOURCES.md)

[English](#english) | [简体中文](#简体中文)

## English

These general resources are not necessarily Fable 5.2 examples. Source links and the limitations below were checked on 12 November 2026 (UTC+8); verify current access and terms before use.

### Asset libraries and production tools

For editable procedural assets and research datasets, see [3D assets as code](../CODE-ASSETS.md#english).

<details>
<summary>Show Asset libraries and production tools</summary>

| Resource | Use | Access and license |
| --- | --- | --- |
| [Astrocade MCP](https://www.astrocade.com/blog/introducing-astrocade-mcp) · [Setup](https://www.astrocade.com/create/mcp) | Connect a coding agent to create, revise and submit games for publication on Astrocade. | Hosted service; account and authorization required, published games are reviewed. The [terms](https://www.astrocade.com/terms-of-service) state personal, non-commercial service use; check current terms and any separate creator-program agreement. Game code export, MCP fees and output rights were not confirmed. Not independently connected or tested. |
| [Origin MCP](https://www.origingame.ai/docs/mcp?hl=en) · [Billing](https://www.origingame.ai/docs/billing?hl=en) | Connect an agent to platform tools for media, assets and web-game publishing. | Hosted; account and browser authorization required. Basic publishing is free; model calls and cloud sandboxes can cost credits. Output rights must be checked separately. Not independently tested. |
| [PlayDrop MCP](https://www.playdrop.ai/create/learn/mcp-publishing) · [License guide](https://www.playdrop.ai/legal/license) | Upload, update and publish games from an AI agent. | Hosted; requires an authorized account. Check visibility before publishing and review each version's license: PLAYDROP-labeled versions have platform-specific reuse restrictions. Service and model costs vary; not independently tested. |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [Documentation](https://sand3d.sandflow.ai/) | Build named, parameterized 3D parts, assemblies and joints in Python over Blender; export to formats including GLB, URDF, USD, OBJ and STL. | Apache-2.0 library; requires compatible Python and Blender `bpy`. General modeling tool, not a Fable 5.2-specific project; not independently run. |
| [Sand3D datasets](https://huggingface.co/collections/Sandflow/sand3d) · [Explorer](https://huggingface.co/spaces/Sandflow/sand3d-explorer) | Browse five collections of code-reconstructed 3D objects and articulated assets; the publisher reports 106,094 objects. | Dataset cards label the Sand3D programs, renders and USD files CC BY 4.0; each object also retains source-license and attribution information. See the source notes below. |
| [Kenney assets](https://kenney.nl/assets) | Game-ready models, sprites, textures and prototyping packs. | [Official support](https://kenney.nl/support) says assets on its asset pages are CC0; check the individual asset's included terms. |
| [3DAssets.dev](https://3dassets.dev/) | Search GLB models and packs from the website or its agent integration. | Site describes its assets as CC0; verify each asset’s provenance and terms. Agent integration not tested here. |
| [Poly Haven](https://polyhaven.com/) | HDRIs, textures and 3D models for lighting and environments. | Its [asset license](https://polyhaven.com/license) states CC0 for its assets. |
| [ambientCG](https://ambientcg.com/) · [API documentation](https://docs.ambientcg.com/api/v3/) | PBR materials, models and HDRIs; the API exposes asset metadata for tooling. | [Official license](https://docs.ambientcg.com/license/) identifies downloadable assets as CC0. API not independently exercised. |
| [KayKit Prototype Bits](https://godotengine.org/asset-library/asset/2122) | Low-poly prototyping meshes using a shared texture atlas. | The creator's Godot Asset Library listing marks this specific pack CC0; check other KayKit packs individually. |
| [LazyTextures](https://www.lazytextures.com/) · [Public API](https://www.lazytextures.com/PublicAPI) | Search materials, models, HDRIs and textures manually or via the documented API. | The site describes its assets as CC0; check asset formats and provenance. API availability was not tested. |
| [Codels](https://codels.download/) | Browse parametric Three.js models as editable code or export GLB, OBJ and STL. | The provider labels the models CC0; verify individual provenance. Agent pages and MCP are documented but have not been tested. |
| [Gobkit](https://gobkit.com/) · [Free asset API](https://gobkit.com/api/free) | Find character and environment GLB assets with machine-readable animation metadata for agent-assisted prototypes. | The provider labels its free packs CC0; verify the license and animation convention for each asset. Generation is a separate paid service; API and models were not independently tested. |
| [Mixamo](https://www.mixamo.com/) | Humanoid character auto-rigging and animation library. | Adobe ID required; the [FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) describes royalty-free uses and says China country-code accounts are unsupported. Check current terms and availability. |
| [Fab](https://www.fab.com/) | Marketplace for 3D models, materials, animations and other assets. | Licenses and prices vary; [Fab's EULA](https://www.fab.com/eula?lang=en) distinguishes its Standard and CC-BY licenses and reference-only tier. |
| [Freesound](https://freesound.org/) | Search sound effects and recordings for games and films. | [Licenses vary by sound](https://freesound.org/help/faq/); check attribution and noncommercial restrictions individually. |
| [Net Forge](https://forge.netnet.capital/docs/guides/build-a-game-with-an-ai-agent) | Multiplayer browser game engine with an agent workflow, templates and a CC0 asset guide. | Engine and documentation claims not independently tested; check each asset’s original license. |
| [OhMyGame](https://www.ohmygame.ai/docs/) | Desktop AI game-development app with browser 3D and engine plugin workflows. | Beta; Apache-2.0 source. Provider accounts and media-generation costs depend on the setup; not independently tested. |
| [Godot AI](https://godotengine.org/asset-library/asset/5050) | Connect MCP clients to a Godot editor for scenes, scripts, materials and tests. | Community plugin, MIT; check the listing for version support and security advisories. |
| [Ziva for Godot](https://ziva.sh/docs/) | Agent in the Godot editor for inspecting scenes, editing scripts and running the game. | Vendor service; access, costs and data handling depend on the chosen plan and provider. Not independently tested. |
| [Meshy DCC Core](https://docs.meshy.ai/en/webapp/plugins/meshy-dcc/introduction) | Connect agents to supported 3D applications through a shared pipeline. | Commercial vendor integration; check supported versions, pricing and generated-asset terms. Not independently tested. |
| [Thrixel MCP](https://thrixel.com/mcp) | Generate and edit 3D assets for agent-assisted game workflows. | Commercial provider; capabilities are vendor claims, not independently tested. Check pricing and asset rights. |
| [Roblox Studio MCP](https://create.roblox.com/docs/studio/mcp) | Connect an AI client to a Studio session for scripting, asset generation and playtests. | Official Studio integration; requires Roblox Studio and a compatible MCP client. |
| [Roblox model generation](https://create.roblox.com/docs/parts/model-generation) | Generate 3D assets from prompts and use preset behavior scripts for functional models. | Roblox-specific; the documented schemas and access may change. |
| [Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor?lang=en-US) | Let a compatible agent work with Unreal Editor tools, including scenes, materials and animation. | Epic labels this feature experimental; API and formats can change. |
| [Blender](https://www.blender.org/) | Model, animate and render 3D scenes and assets. | Free/open-source production software; its license does not establish the rights to third-party assets. |

</details>

**Sand3D dataset sources:** [Objaverse](https://huggingface.co/datasets/Sandflow/sand3d-objaverse), [CAD](https://huggingface.co/datasets/Sandflow/sand3d-cad), [Articraft](https://huggingface.co/datasets/Sandflow/sand3d-articraft), [AutoMate](https://huggingface.co/datasets/Sandflow/sand3d-automate), and [NVIDIA SimReady](https://huggingface.co/datasets/Sandflow/sand3d-simready). The publisher says each record includes its `source_license` and `attribution`; check these and retain the required notices and modification information. The CADFS portion of CAD and AutoMate derive from public Onshape designs whose authors may hold rights not covered by the source license, according to their dataset cards. The 106,094-object total is the publisher's reported snapshot, not an independently counted inventory; the explorer is a sample, not the complete collection, and was paused when checked on 12 November 2026 (UTC+8).


## 简体中文

这些是通用资源，不一定使用了 Fable 5.2。来源链接与下文记载的限制核查于 2026 年 11 月 12 日（UTC+8）；使用前请核对当前访问条件和条款。

### 资产库与制作工具

可编辑的程序化资产和研究数据集见[代码构建的 3D 资产](../CODE-ASSETS.md#简体中文)。

<details>
<summary>展开 资产库与制作工具</summary>

| 资源 | 用途 | 访问与许可 |
| --- | --- | --- |
| [Astrocade MCP](https://www.astrocade.com/blog/introducing-astrocade-mcp) · [配置指南](https://www.astrocade.com/create/mcp) | 将编程智能体接入 Astrocade，创建、修改游戏并提交平台发布。 | 托管服务，需要账号和授权；发布的游戏须经审核。[服务条款](https://www.astrocade.com/terms-of-service)写明服务仅供个人非商业用途，使用前应核对最新条款及可能另行适用的创作者计划协议。游戏源码导出、MCP 费用和产物权利尚未确认；未独立连接或测试。 |
| [Origin MCP](https://www.origingame.ai/docs/mcp?hl=en) · [计费说明](https://www.origingame.ai/docs/billing?hl=en) | 将智能体连接到媒体生成、素材和网页游戏发布工具。 | 托管服务，需要账号和浏览器授权。基础发布免费，模型调用和云沙箱可能消耗额度；生成结果权利需另行核对。尚未独立测试。 |
| [PlayDrop MCP](https://www.playdrop.ai/create/learn/mcp-publishing) · [许可指南](https://www.playdrop.ai/legal/license) | 通过 AI 智能体上传、更新和发布游戏。 | 托管服务，需要授权账号。发布前检查可见性及各版本许可：标为 PLAYDROP 的版本有平台内复用限制。服务和模型费用因使用方式而异；尚未独立测试。 |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [文档](https://sand3d.sandflow.ai/) | 基于 Blender 的 Python 接口，用代码创建具名、可调参数的 3D 零件、装配体和关节，并导出 GLB、URDF、USD、OBJ、STL 等格式。 | 建模库采用 Apache-2.0，需要兼容的 Python 与 Blender `bpy`。这是通用建模工具，并非 Fable 5.2 专属；尚未独立运行。 |
| [Sand3D 数据集](https://huggingface.co/collections/Sandflow/sand3d) · [在线浏览](https://huggingface.co/spaces/Sandflow/sand3d-explorer) | 查找五组以代码重建的 3D 对象和可动资产；发布方称共 106,094 个对象。 | 数据卡将 Sand3D 程序、渲染图和 USD 文件标为 CC BY 4.0；每个对象还保留来源许可和署名信息，详见下方来源说明。 |
| [Kenney 资产库](https://kenney.nl/assets) | 游戏模型、精灵、纹理和原型素材包。 | [官方说明](https://kenney.nl/support)称资产页上的游戏素材采用 CC0；仍应查看具体素材附带的条款。 |
| [3DAssets.dev](https://3dassets.dev/) | 从网站或智能体接口查找 GLB 模型和素材包。 | 网站称其资产为 CC0；请逐项核对来源及条款。智能体接口尚未测试。 |
| [Poly Haven](https://polyhaven.com/) | HDRI、纹理和 3D 模型，适合环境与灯光制作。 | 其[资产许可](https://polyhaven.com/license)说明站内素材采用 CC0。 |
| [ambientCG](https://ambientcg.com/) · [API 文档](https://docs.ambientcg.com/api/v3/) | PBR 材质、模型和 HDRI；可通过 API 查询资产元数据。 | [官方许可](https://docs.ambientcg.com/license/)将可下载资产标为 CC0；未独立测试 API。 |
| [KayKit Prototype Bits](https://godotengine.org/asset-library/asset/2122) | 使用共享纹理图集的低多边形原型模型。 | 创作者在 Godot 资产库中将这个素材包标为 CC0；其他 KayKit 素材包需逐项核对。 |
| [LazyTextures](https://www.lazytextures.com/) · [公开 API](https://www.lazytextures.com/PublicAPI) | 手动或通过文档所述 API 查找材质、模型、HDRI 和纹理。 | 网站称其资产为 CC0；使用前核对格式与来源。API 可用性尚未独立测试。 |
| [Codels](https://codels.download/) | 查找可编辑代码形式的参数化 Three.js 模型，也可导出 GLB、OBJ 和 STL。 | 网站将模型标为 CC0；请核对具体来源。智能体页面与 MCP 功能有文档说明，但尚未测试。 |
| [Gobkit](https://gobkit.com/) · [免费资产 API](https://gobkit.com/api/free) | 查找角色和环境 GLB 资产及可供智能体读取的动画元数据，用于制作原型。 | 服务方将免费素材包标为 CC0；请逐项核对许可证和动画约定。生成服务另行收费，API 和模型尚未独立测试。 |
| [Mixamo](https://www.mixamo.com/) | 人形角色自动绑定和动作库。 | 需要 Adobe ID；[官方问答](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)说明免版税用途，并称不支持中国地区代码的账户。请核对当前条款和可用性。 |
| [Fab](https://www.fab.com/) | 3D 模型、材质、动画等资产市场。 | 价格和许可依素材而异；[Fab EULA](https://www.fab.com/eula?lang=en)区分标准许可、CC-BY 和仅引用层级。 |
| [Freesound](https://freesound.org/) | 查找适用于游戏和影片的音效与录音。 | [各音频许可不同](https://freesound.org/help/faq/)，需逐项核对署名及非商业限制。 |
| [Net Forge](https://forge.netnet.capital/docs/guides/build-a-game-with-an-ai-agent) | 面向浏览器多人游戏的引擎，提供智能体工作流、模板和 CC0 素材指南。 | 引擎及文档中的效果尚未独立测试；素材仍需核对原始许可。 |
| [OhMyGame](https://www.ohmygame.ai/docs/) | 支持浏览器 3D 和引擎插件工作流的桌面 AI 游戏开发工具。 | 测试版；源码为 Apache-2.0。模型账户及媒体生成费用取决于配置，尚未独立测试。 |
| [Godot AI](https://godotengine.org/asset-library/asset/5050) | 将 MCP 客户端连接到 Godot 编辑器，处理场景、脚本、材质和测试。 | 社区插件，MIT；请查看页面中的版本支持和安全公告。 |
| [Ziva for Godot](https://ziva.sh/docs/) | 在 Godot 编辑器内检查场景、编辑脚本并运行游戏的智能体。 | 厂商服务；访问、费用和数据处理取决于计划与模型提供方，尚未独立测试。 |
| [Meshy DCC Core](https://docs.meshy.ai/en/webapp/plugins/meshy-dcc/introduction) | 通过统一流程将智能体连接到支持的 3D 制作软件。 | 商业厂商集成；请核对软件版本、价格和生成资产条款。尚未独立测试。 |
| [Thrixel MCP](https://thrixel.com/mcp) | 在智能体辅助的游戏制作流程中生成和编辑 3D 资产。 | 商业服务；能力依据厂商说明，尚未独立测试。使用前核对价格和资产权利。 |
| [Roblox Studio MCP](https://create.roblox.com/docs/studio/mcp) | 将 AI 客户端连接到 Studio，辅助写脚本、生成资产和试玩。 | Roblox 官方集成，需要 Studio 和兼容的 MCP 客户端。 |
| [Roblox 模型生成](https://create.roblox.com/docs/parts/model-generation) | 通过提示词生成 3D 资产，并用预设行为脚本制作可交互模型。 | 适用于 Roblox；所支持的模型结构和访问条件可能变化。 |
| [Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor?lang=en-US) | 让兼容智能体调用 Unreal Editor 工具，操作场景、材质和动画等。 | Epic 将其标为实验性功能，API 和数据格式可能变化。 |
| [Blender](https://www.blender.org/) | 制作模型、动画并渲染 3D 场景和资产。 | 免费开源制作软件；软件许可不等于第三方资产的使用许可。 |

</details>

**Sand3D 数据集来源：**[Objaverse](https://huggingface.co/datasets/Sandflow/sand3d-objaverse)、[CAD](https://huggingface.co/datasets/Sandflow/sand3d-cad)、[Articraft](https://huggingface.co/datasets/Sandflow/sand3d-articraft)、[AutoMate](https://huggingface.co/datasets/Sandflow/sand3d-automate) 和 [NVIDIA SimReady](https://huggingface.co/datasets/Sandflow/sand3d-simready)。发布方说明每条记录包含 `source_license` 和 `attribution`；使用时应检查并保留所需的许可、署名与修改说明。CAD 中的 CADFS 部分和 AutoMate 来自公开的 Onshape 设计，其数据卡提示原设计作者可能拥有来源许可证未覆盖的权利。106,094 是发布方报告的数量快照，并非本项目独立清点；在线浏览器展示的是样例，不是完整资产库；2026 年 11 月 12 日（UTC+8）检查时该 Space 处于暂停状态。

# Skills, Tutorials & Creator Advice / Skills、教程与创作者经验

[English](#english) | [简体中文](#简体中文)

## English

Resources for making code-driven 3D games, scenes, interactive experiences and films. They are **not all Fable 5.2 examples**: the model or tools are named when the source identifies them; otherwise they are general techniques. This is a curated starting point, not an endorsement or a claim that the resources were used by projects in the main catalog. Links were checked on 12 November 2026 (UTC+8), subject to the access limits below.

### Agent Skills

| Resource | Best for | Notes |
| --- | --- | --- |
| [img2threejs](https://github.com/img2threejs/img2threejs) · [SKILL.md](https://github.com/img2threejs/img2threejs/blob/main/SKILL.md) | Reconstructing objects from reference images as procedural Three.js code, with geometry and visual review. | Apache-2.0. The [island workflow below](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/) reports using it for small props; its larger terrain and cabin used separate image-to-3D tools. |
| [Three.js Game Skills](https://github.com/majidmanzarpour/threejs-game-skills) | A coordinated browser-game workflow covering gameplay, graphics, interface and verification. | MIT; repository description and capabilities are maintainer claims, not independent tests. |
| [Blender Game Skills](https://github.com/majidmanzarpour/blender-game-skills) | Blender-based game assets, from reference to modeled and rigged assets. | MIT; designed for Claude Code and Blender. Check the project's setup and applicable tool versions. |
| [Awesome GameDev Agent Skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | Browse skills across engines, including Three.js, and game-design disciplines. | Apache-2.0. The repository's engine testing claims have not been independently reproduced here. |
| [World Builder](https://github.com/Top3d-ai/world-builder) | Compose a stylized Blender scene from a reference, with procedural terrain, placement and iterative visual checks. | License not confirmed. Requires a live Blender/MCP setup; its example also uses commercial generation services. |
| [Blender AI Plugin](https://github.com/proyecto26/blender-ai-plugin) | Blender MCP skills for asset production and engine export. | MIT; maintainer reports tests, not independently reproduced. |
| [Blender Skill](https://github.com/kajisho5/blender-skill) | Inspect, convert, optimize and render 3D assets using local headless Blender. | MIT; local Blender required. Maintainer-described workflow, not independently executed. |
| [Three.js Lab Skills](https://github.com/LumosLab-Innovation/3D-lab-skills) | Build interactive models with Three.js or Blender and add Three.js motion. | GPL-3.0; review its terms and setup. Compatibility claims are from the maintainer. |
| [Image-to-3D Rebuild](https://github.com/undeadpickle/image-to-3d-rebuild) | Use a generated rough mesh as a reference to rebuild and animate a cleaner Godot asset, then make a web viewer. | MIT; the documented workflow needs Godot and a 3D generation service. Tested example is a hard-surface treasure chest. |
| [Video to Game](https://github.com/lovisdotio/video-to-game) | Study a gameplay concept clip and build a playable Three.js game with visual comparison and playtesting. | MIT; upstream workflow uses fal for generated assets. A [separately adapted version](https://gameskill.dev/skills/video-to-game) describes an optional no-key fallback; neither version has been run here. |
| [Every Frame Is Code](https://github.com/kiselas/every-frame-is-code) | Build code-based 3D scenes, games and motion graphics, with frame-by-frame video rendering. | MIT; repository workflow has not been independently tested. |
| [Bang Motion](https://github.com/RFTaurus/motion-skill) | Create browser-based motion graphics and explainers as playable HTML. | Check the repository license and tool requirements; not independently tested. |
| [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) | Code-driven video, animation, rendering and 3D map flyovers. | Official documentation; check Remotion’s own license and pricing for the intended use. |
| [Meta VR agent skills and CLI](https://developers.meta.com/vr/essentials/ai-tooling-overview/) | Device workflows, logs, performance traces and asset discovery for Meta VR development. | Official device-specific tooling; requires the appropriate device and setup. |
| [PlayCanvas Skills](https://developer.playcanvas.com/user-manual/getting-started/use-playcanvas-skills/) | Build and validate code-based browser 3D scenes and games with PlayCanvas. | Official skills for Engine, React and Web Components; Editor projects require a separate MCP route. |
| [Godot Indie Game Skill](https://github.com/ProfesseurHaipeng/godot-indie-game-skill) | Build a runnable Godot 4 game slice with 3D controls and visual checks. | MIT; maintainer-described checks, not independently run. |
| [Scenario Labs Skills](https://github.com/scenario-labs/skills) | Agent skills for 3D production and game assets across supported creative tools. | MIT repository; some workflows use Scenario MCP and paid generation services. Not independently tested. |
| [Unity agent plugin](https://docs.unity.com/en-us/ai/unity-plugin/about-unity-plugin) | Unity-maintained skills for coding agents, covering UI, multiplayer, rendering and other Unity tasks. | Requires Unity 6.0 or later; consult individual skill scope. |
| [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill) | Use Spline MCP to create and maintain editable interactive 3D scenes. | Vendor documentation; requires the Spline integration. Skill license not independently confirmed. |
| [Varg video skills](https://github.com/vargHQ/skills) | Explore the repository's code-film, 3D explainer and Three.js animatic skills. | MIT; a vendor collection with optional paid services. Individual skills and their external dependencies have not been run here. |

Read each skill and its dependencies before use. Linking a skill does not install it or establish that it suits every engine version or project. Licenses cover the linked repositories, not automatically any assets or games made using them.

### Asset libraries and production tools

| Resource | Use | Access and license |
| --- | --- | --- |
| [Kenney assets](https://kenney.nl/assets) | Game-ready models, sprites, textures and prototyping packs. | [Official support](https://kenney.nl/support) says assets on its asset pages are CC0; check the individual asset's included terms. |
| [3DAssets.dev](https://3dassets.dev/) | Search GLB models and packs from the website or its agent integration. | Site describes its assets as CC0; verify each asset’s provenance and terms. Agent integration not tested here. |
| [Poly Haven](https://polyhaven.com/) | HDRIs, textures and 3D models for lighting and environments. | Its [asset license](https://polyhaven.com/license) states CC0 for its assets. |
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

### Reddit: workflows and critiques

| Source | Practical takeaways | Scope and limits |
| --- | --- | --- |
| [Animated island with Claude Code and img2threejs](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/) · u/Quirky_Success8287 | Use a reference and separate prop sheet; review props individually; simplify larger imported meshes and rebake normal maps; keep a boat synchronized with the water's wave function. | Creator-reported workflow and measurements; the scoring threshold is the creator's own. Model version not specified in the post. |
| [Code-generated walkable street](https://www.reddit.com/r/TopologyAI/comments/1vobf1y/an_llm_generated_this_complete_3d_scene_in_the/) · u/Certain_Friendship16 | The post links [source and five prompts](https://github.com/StarKnightt/night-street). Comments question whether building and vehicle geometry makes sense up close; inspect geometry rather than judging only a moving preview. | Claude and Three.js/R3F; specific Claude version not stated in the post. Useful as a prototype and critique, not evidence of production quality. |
| [3D roguelite: three sessions and a playtest](https://www.reddit.com/r/aigamedev/comments/1vjv3z8/i_left_claude_code_running_for_24h_it_built_a_3d/) · u/victorrseloy2 | The creator describes a base build, a follow-up after a real playtest, then a finishing session; the post links the original prompt and describes a deterministic frame-by-frame trailer. | Creator says Opus 5, existing Kenney/KayKit assets and generated audio were also used. It was not a single uninterrupted prompt; performance and cost are author reports. |
| [Browser FPS with code-generated models](https://www.reddit.com/r/ClaudeAI/comments/1x8dg94/i_made_a_browser_fps_with_claude_code_every_3d/) · u/Inevitable_Salad_128 | The creator iterated a Three.js FPS over about a month and generated models in code; the discussion considers mobile, controller support and alternative asset pipelines. | Creator names Opus 5.5 and Sonnet 5.5, not Fable 5.2. Other commenters' pipelines are their own, not the author's. |
| [Image-to-3D reference and rebuild workflow](https://www.reddit.com/r/aigamedev/comments/1xa3gju/new_crazy_workflow_for_making_3d_assets/) · u/FearlessCounty3487 and u/mr_undeadpickle77 | The original poster describes importing a generated rough model into Godot and rebuilding it; a commenter documented a separate Meshy → Godot → interactive preview workflow and published a skill. | Both are individual accounts. The commenter names Opus 5.5, GPT Image 2.5 and Meshy 7; generated assets and services have their own terms. |

### X and developer tutorials

| Source | Practical use | Scope and limits |
| --- | --- | --- |
| [Sunny Valley Studio on X: Claude Code + Unity MCP 3D platformer](https://x.com/SunnyVStudio/status/2061879369950282060) · [linked tutorial](https://youtu.be/gSFHyso_uuI) | Entry point to a Unity 3D platformer prototyping tutorial. | The post text was visible in search; X returned 403 and the video was throttled when checked. Detailed steps and model version were not independently verified. |
| [Meta Model API: iterative game dev](https://dev.meta.ai/docs/cookbook/iterative-game-dev) | Build a Three.js racing game with existing 3D assets and a browser playtest/refinement loop. | Vendor cookbook using Muse Spark, OpenCode and Playwright MCP; API access required. The page gives inconsistent model-version references. |
| [Meta Horizon: GenAI Assistant scripting](https://developers.meta.com/horizon-worlds/learn/videos/unlocking-worlds-with-genai-assistant/) | Practice generating, refining and testing interactive world scripts from prompts. | Official Horizon Worlds tutorial; requires its desktop editor on Windows. |
| [Roblox: AI Assistant tutorial](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant) | Ask Studio’s assistant to modify 3D object behavior, then review and playtest its code. | Official Roblox-specific beginner tutorial; not a Fable 5.2 example. |
| [AI Game Dev tutorials](https://aigamedev.ai/tutorials/) | General AI-assisted game prototyping, gameplay and playtesting tutorials. | Mostly general or 2D examples; useful transferable practice, not a dedicated Fable 5.2 / 3D guide. |
| [Three.js manual: Making a Game](https://threejs.org/manual/pages/game.html) | Load assets with progress reporting, organize animation and explicitly plan input, physics and other game systems. | General engineering tutorial, not AI-specific. The manual stresses that Three.js is a 3D library rather than a complete game engine. |
| [Three.js manual: Shadows](https://threejs.org/manual/pages/shadows.html) | Budget shadow-casting lights and objects; shadow maps render casters from each light's viewpoint. | General rendering guidance; profile the actual target device. |
| [Bruno Simon: interactive portfolio and devlogs](https://www.bruno-simon.com/) | Explore a driveable Three.js world and the creator’s links to development logs and source. | General creative-development reference, not an AI or Fable 5.2 tutorial; the author says server code is excluded. |
| [Meshy: asset placement in Unreal](https://www.meshy.ai/developers/cookbook/recipes/place-3d-asset-in-unreal/) | Generate a concept and model, place it with Unreal MCP, then inspect it in play mode. | Paid vendor workflow; documented test was on macOS with Unreal 5.8.2. Not independently reproduced. |
| [Meshy: Three.js browser game workflow](https://www.meshy.ai/tutorials/make-a-3d-browser-game-with-threejs) | Follow a 3D chess example from generated assets and animation to a browser game. | Vendor tutorial; Meshy features can have costs. Claims and results have not been independently reproduced. |
| [3D Valley: playable island from asset libraries](https://3dvalley.com/tutorials/make-a-3d-game-with-ai) | Compare kit, scale, rigging and animation metadata while choosing assets for a Three.js prototype. | Vendor tutorial; check each source asset and access conditions. |
| [Playloop: AI agent and Blender asset pipeline](https://playloop.gg/learn/3d-pipeline) | Follow a reference-image → 3D generation → Blender cleanup → GLB workflow, with visual checks. | Vendor tutorial; example uses paid Tripo and lists a local alternative. Not independently reproduced. |
| [Serafin Sanchez / Meshy: Game assets with Blender MCP](https://www.meshy.ai/developers/blog/blender-mcp-meshy-game-assets/) | Set a shared visual style, specify scale, use multiple views for important objects and define triangle budgets before export. | Vendor tutorial using Claude Code and Meshy; paid service and product-specific claims. Its stated results are one workflow, not an independent comparison. |

For community feedback on the catalog's works, see [Community Feedback & Trends](COMMUNITY-FEEDBACK.md#english). Search and access limitations for the case collection are in the [search log](SEARCH-LOG.md).

## 简体中文

这里收集制作代码驱动的 3D 游戏、场景、互动体验和影片时可参考的资源。**并非所有资源都使用 Fable 5.2**：来源明确说明时才标注模型或工具，其余作为通用方法。这里是经过筛选的起点，不代表我们已验证每个 Skill 的效果，也不意味着案例库中的作品都使用了这些资源。链接于 2026 年 11 月 12 日（北京时间）检查，访问限制见下文。

### Agent Skills

| 资源 | 适合做什么 | 说明 |
| --- | --- | --- |
| [img2threejs](https://github.com/img2threejs/img2threejs) · [SKILL.md](https://github.com/img2threejs/img2threejs/blob/main/SKILL.md) | 根据参考图用程序化 Three.js 代码重建物体，并做几何和视觉检查。 | Apache-2.0。下方[岛屿案例](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/)的作者说小道具使用了它；较复杂的地形和房屋另用了图生 3D 工具。 |
| [Three.js Game Skills](https://github.com/majidmanzarpour/threejs-game-skills) | 组织浏览器游戏的玩法、画面、界面和验证工作。 | MIT；能力范围依据维护者介绍，尚未独立运行测试。 |
| [Blender Game Skills](https://github.com/majidmanzarpour/blender-game-skills) | 从参考图出发，在 Blender 中制作、绑定游戏 3D 资产。 | MIT；面向 Claude Code 和 Blender，使用前应核对项目说明及工具版本。 |
| [Awesome GameDev Agent Skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 查找 Three.js 等引擎及游戏设计领域的技能。 | Apache-2.0；仓库对引擎测试的说明尚未经本项目独立复现。 |
| [World Builder](https://github.com/Top3d-ai/world-builder) | 参考图片在 Blender 中组合风格化场景，包括程序化地形、物件摆放和迭代检查。 | 许可未确认；需要运行 Blender/MCP，示例还使用商业生成服务。 |
| [Blender AI Plugin](https://github.com/proyecto26/blender-ai-plugin) | 借助 Blender MCP 制作资产并导出到游戏引擎。 | MIT；维护者报告了测试，本项目尚未独立复现。 |
| [Blender Skill](https://github.com/kajisho5/blender-skill) | 使用本地无界面的 Blender 检查、转换、优化和渲染 3D 资产。 | MIT；需要本地 Blender。流程来自维护者介绍，尚未独立运行。 |
| [Three.js Lab Skills](https://github.com/LumosLab-Innovation/3D-lab-skills) | 使用 Three.js 或 Blender 制作交互模型，并用 Three.js 添加动态效果。 | GPL-3.0；使用前阅读许可和设置说明。兼容性依据维护者介绍。 |
| [Image-to-3D Rebuild](https://github.com/undeadpickle/image-to-3d-rebuild) | 用生成的粗模作参考，在 Godot 中重建和制作动画，再生成网页查看器。 | MIT；所述流程需要 Godot 和 3D 生成服务。示例验证的是硬表面宝箱。 |
| [Video to Game](https://github.com/lovisdotio/video-to-game) | 分析原创游戏概念视频，用 Three.js 制作可试玩作品并进行画面对照和试玩。 | MIT；上游流程使用 fal 生成资产。[另一个改编版本](https://gameskill.dev/skills/video-to-game)说明了无需密钥的可选替代方案；均未独立运行。 |
| [Every Frame Is Code](https://github.com/kiselas/every-frame-is-code) | 用代码制作 3D 场景、游戏与动态图形，并逐帧渲染视频。 | MIT；仓库流程尚未独立测试。 |
| [Bang Motion](https://github.com/RFTaurus/motion-skill) | 制作可在浏览器播放的代码生成的动态视觉与解说作品。 | 请查看仓库许可与工具要求；尚未独立测试。 |
| [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) | 用代码制作视频和动画、渲染成片，以及制作 3D 地图飞行镜头。 | 官方文档；应按用途核对 Remotion 自身的许可和价格。 |
| [Meta VR agent skills 与 CLI](https://developers.meta.com/vr/essentials/ai-tooling-overview/) | 面向 Meta VR 的设备操作、日志、性能分析和资产查找。 | 官方设备专用工具，需要相应设备和配置。 |
| [PlayCanvas Skills](https://developer.playcanvas.com/user-manual/getting-started/use-playcanvas-skills/) | 使用 PlayCanvas 编写并验证浏览器 3D 场景和游戏。 | 官方 Skills 适用于 Engine、React 与 Web Components；Editor 项目需另用 MCP。 |
| [Godot Indie Game Skill](https://github.com/ProfesseurHaipeng/godot-indie-game-skill) | 构建可运行的 Godot 4 游戏原型，包含 3D 控制与画面检查。 | MIT；检查方法来自维护者说明，尚未独立运行。 |
| [Scenario Labs Skills](https://github.com/scenario-labs/skills) | 在支持的创意工具中制作游戏资产和 3D 作品的智能体技能。 | 仓库为 MIT；部分流程使用 Scenario MCP 及付费生成服务，尚未独立测试。 |
| [Unity agent plugin](https://docs.unity.com/en-us/ai/unity-plugin/about-unity-plugin) | Unity 官方为编程智能体提供的 Skills，涵盖 UI、多人、渲染等任务。 | 需要 Unity 6.0 或更新版本；具体能力以各 Skill 为准。 |
| [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill) | 通过 Spline MCP 制作和维护可编辑的交互式 3D 场景。 | 厂商文档；需要连接 Spline。Skill 许可尚未独立核实。 |
| [Varg video skills](https://github.com/vargHQ/skills) | 查找代码影片、3D 解说和 Three.js 动态预演相关技能。 | MIT；厂商技能集合，部分服务可能收费；具体 Skill 与外部依赖尚未运行测试。 |

使用前应阅读具体 Skill 和依赖。收录链接不等于安装，也不保证其适合所有引擎版本或项目。标注的许可仅指链接仓库，不自动覆盖用它制作的资产或游戏。

### 资产库与制作工具

| 资源 | 用途 | 访问与许可 |
| --- | --- | --- |
| [Kenney 资产库](https://kenney.nl/assets) | 游戏模型、精灵、纹理和原型素材包。 | [官方说明](https://kenney.nl/support)称资产页上的游戏素材采用 CC0；仍应查看具体素材附带的条款。 |
| [3DAssets.dev](https://3dassets.dev/) | 从网站或智能体接口查找 GLB 模型和素材包。 | 网站称其资产为 CC0；请逐项核对来源及条款。智能体接口尚未测试。 |
| [Poly Haven](https://polyhaven.com/) | HDRI、纹理和 3D 模型，适合环境与灯光制作。 | 其[资产许可](https://polyhaven.com/license)说明站内素材采用 CC0。 |
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

### Reddit：工作流与反面意见

| 来源 | 值得参考的做法 | 适用范围与限制 |
| --- | --- | --- |
| [用 Claude Code 和 img2threejs 制作动态岛屿](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/) · u/Quirky_Success8287 | 准备参考图和分物件素材图，逐项检查小道具；简化较大的导入模型后重新烘焙法线贴图；让船与海水使用同一套波浪函数。 | 流程和性能数字来自作者自述；评分门槛是作者自己的选择。帖子未注明具体模型版本。 |
| [纯代码生成的可漫游街景](https://www.reddit.com/r/TopologyAI/comments/1vobf1y/an_llm_generated_this_complete_3d_scene_in_the/) · u/Certain_Friendship16 | 帖子链接了[源码和五条提示词](https://github.com/StarKnightt/night-street)。评论者指出建筑和车辆的局部结构可能不合理，提醒我们近距离检查几何，而不仅看移动镜头。 | 使用 Claude 和 Three.js/R3F；帖子未注明 Claude 具体版本。适合作为原型与批评案例，不代表达到产品级质量。 |
| [3D Roguelite：分三次构建并穿插试玩](https://www.reddit.com/r/aigamedev/comments/1vjv3z8/i_left_claude_code_running_for_24h_it_built_a_3d/) · u/victorrseloy2 | 作者描述先做基础版本、实际试玩后继续迭代，再做收尾；帖子提供原始提示词，并介绍逐帧生成预告片的方法。 | 作者称使用 Opus 5，也使用了现成 Kenney/KayKit 资产和生成音频；并非单次不间断提示。性能与成本为作者自述。 |
| [浏览器 FPS：模型由代码生成](https://www.reddit.com/r/ClaudeAI/comments/1x8dg94/i_made_a_browser_fps_with_claude_code_every_3d/) · u/Inevitable_Salad_128 | 作者用约一个月迭代 Three.js FPS，直接用代码生成模型；讨论还涉及手机、手柄和其他资产制作流程。 | 作者提及 Opus 5.5 和 Sonnet 5.5，而非 Fable 5.2。其他评论者的资产管线属于其个人经验，不应归给原作者。 |
| [用图生粗模作参考，再重建 3D 资产](https://www.reddit.com/r/aigamedev/comments/1xa3gju/new_crazy_workflow_for_making_3d_assets/) · u/FearlessCounty3487 与 u/mr_undeadpickle77 | 原帖作者介绍先把生成粗模导入 Godot 再重建；另一位评论者记录了自己的 Meshy → Godot → 交互预览流程，并发布了对应 Skill。 | 均为个人经验；评论者注明使用 Opus 5.5、GPT Image 2.5 和 Meshy 7。生成资产及服务需分别核对条款。 |

### X 与开发者教程

| 来源 | 值得参考的内容 | 适用范围与限制 |
| --- | --- | --- |
| [Sunny Valley Studio 的 X 帖：Claude Code + Unity MCP 制作 3D 平台游戏](https://x.com/SunnyVStudio/status/2061879369950282060) · [关联教程](https://youtu.be/gSFHyso_uuI) | 使用 Unity 快速制作 3D 平台游戏原型的教程入口。 | 搜索结果可见帖子文字；检查时 X 返回 403，视频被限流，具体步骤和模型版本未能独立核实。 |
| [Meta Model API：迭代制作游戏](https://dev.meta.ai/docs/cookbook/iterative-game-dev) | 使用现有 3D 资产制作 Three.js 赛车游戏，并通过浏览器试玩反复调整。 | 厂商教程，使用 Muse Spark、OpenCode 和 Playwright MCP，需要 API；页面中的模型版本表述不一致。 |
| [Meta Horizon：GenAI Assistant 脚本教程](https://developers.meta.com/horizon-worlds/learn/videos/unlocking-worlds-with-genai-assistant/) | 练习通过提示词生成、修改和测试互动世界脚本。 | Horizon Worlds 官方教程；需要 Windows 和其桌面编辑器。 |
| [Roblox：AI Assistant 教程](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant) | 让 Studio 助手修改 3D 物体行为，再阅读代码并试玩验证。 | Roblox 官方入门教程，并非 Fable 5.2 案例。 |
| [AI Game Dev 教程](https://aigamedev.ai/tutorials/) | AI 辅助游戏原型、玩法和试玩的通用教程。 | 示例多为通用或 2D，可借鉴方法；并非 Fable 5.2 / 3D 专题。 |
| [Three.js 手册：制作游戏](https://threejs.org/manual/pages/game.html) | 了解资产加载进度、动画组织，以及输入、物理等游戏系统需要如何另行规划。 | 通用工程教程，并非 AI 专用。手册强调 Three.js 是 3D 库，而非完整游戏引擎。 |
| [Three.js 手册：阴影](https://threejs.org/manual/pages/shadows.html) | 为投影光源和物体规划性能预算；阴影贴图需要从光源视角渲染投影物体。 | 通用渲染知识；应在实际目标设备上测量。 |
| [Bruno Simon：交互式个人网站与开发日志](https://www.bruno-simon.com/) | 体验可驾驶探索的 Three.js 世界，并从作者页面查找开发日志和源码。 | 通用创意开发参考，不是 AI 或 Fable 5.2 教程；作者说明未公开服务端代码。 |
| [Meshy：在 Unreal 中放置生成资产](https://www.meshy.ai/developers/cookbook/recipes/place-3d-asset-in-unreal/) | 生成概念图和模型，通过 Unreal MCP 放入场景，再在试玩模式中检查。 | 付费厂商流程；文中测试环境为 macOS 与 Unreal 5.8.2，尚未独立复现。 |
| [Meshy：Three.js 浏览器游戏流程](https://www.meshy.ai/tutorials/make-a-3d-browser-game-with-threejs) | 以 3D 国际象棋为例，从生成资产和动画做到浏览器游戏。 | 厂商教程；Meshy 功能可能收费，文中结果尚未独立复现。 |
| [3D Valley：用资产库制作可玩岛屿](https://3dvalley.com/tutorials/make-a-3d-game-with-ai) | 为 Three.js 原型挑选素材时，对照素材包、尺寸、绑定和动画信息。 | 厂商教程；应分别核对原素材与访问条件。 |
| [Playloop：AI 智能体与 Blender 资产流程](https://playloop.gg/learn/3d-pipeline) | 按参考图、3D 生成、Blender 清理和 GLB 导出的顺序制作资产，并检查渲染结果。 | 厂商教程；示例使用付费 Tripo，也列出本地替代方案。尚未独立复现。 |
| [Serafin Sanchez / Meshy：用 Blender MCP 制作游戏资产](https://www.meshy.ai/developers/blog/blender-mcp-meshy-game-assets/) | 统一视觉风格、指定尺寸，为重要物体准备多视图，并在导出前设定三角面预算。 | 厂商教程，使用 Claude Code 和 Meshy；涉及付费服务及产品特定说明。文中结果只是一次工作流，不是独立对照实验。 |

案例库内的作品反馈见[社区反馈与趋势](COMMUNITY-FEEDBACK.md#简体中文)；案例检索与访问限制见[检索记录](SEARCH-LOG.md)。

# Agent Skills / 智能体技能

[Resource directory / 资源目录](../RESOURCES.md)

[English](#english) | [简体中文](#简体中文)

## English

These general resources are not necessarily Fable 5.2 examples. Source links and the limitations below were checked on 12 November 2026 (UTC+8); verify current access and terms before use.

### Agent Skills

| Resource | Best for | Notes |
| --- | --- | --- |
| [Blender Skills](https://github.com/EL4CTEO/blender-skills) | Blender modeling, rigging, materials, optimization and export skills. | MIT; requires Blender and optionally an MCP connection. Maintainer-reported tests were not independently run. |
| [Open Game Skills](https://github.com/jammyfu/open-game-skills) | Explore game-feel, camera, combat and engine-specific implementation skills. | MIT; Python and target-engine requirements vary. The maintainer notes that CI does not establish agent routing or playability. Not independently run. |
| [BlenderXAlpha 3DGenSkill](https://github.com/ig-shadow-walker/BlenderXAlpha-3DGenSkill) | Generate and place 3D assets in Blender using supported provider integrations. | MIT; Blender MCP, provider account and credits may be required. Inspect the skill's cost and approval steps; not independently run. |
| [Godot Stagehand](https://github.com/mrf/godot-stagehand) · [Skill](https://github.com/mrf/godot-stagehand/blob/main/integrations/claude-code/skills/stagehand/SKILL.md) | Run Godot playtest scenarios, input replay and screenshot comparisons locally or in CI. | MIT; pre-1.0; requires a configured Godot addon and tools. Maintainer-described behavior not independently tested. |
| [Game development shipping skill](https://github.com/ericrisco/rsc-harness/blob/main/skills/gamedev-shipping/SKILL.md) | Consult engine-specific build, signing and release workflows. | MIT repository; platform accounts and toolchains vary. Versioned guidance may be stale; check current platform documentation. Not independently run. |
| [Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Explore Remotion-based shot planning and editable product-video workflows. | Apache-2.0 repository; Node, FFmpeg and optional tools are required. Check Remotion and individual media licenses; not independently run. |
| [image-blaster](https://github.com/neilsonnn/image-blaster) · [Creator’s X demonstration](https://x.com/neilsonks/status/2055013782771134479) | Explore a Claude skill workflow that separates a source image into a static world, object meshes and sound effects. | MIT repository. Its documented workflow uses Claude, World Labs and FAL; service costs and output rights vary. Not run here; the X post returned 403. |
| [Codex GameDev Kit](https://github.com/IlyasGameDev/codex-gamedev-kit) | Browse game-development skills and roles for Unity, Godot and Unreal workflows. | MIT; designed for OpenAI Codex and requires the relevant engine/tool setup. Maintainer claims and workflows not independently tested. |
| [Makone](https://github.com/wormholeportal/Makone) | Create procedural Three.js worlds with an agent workflow, screenshot review and browser checks. | MIT; the repository describes an integrated runtime, examples and validation harness. Not independently run. |
| [Gua](https://github.com/gua-project/gua) | Automate Godot and Unity playtests through semantic scene inspection, inputs, recording and MCP. | MIT; requires a supported engine setup. Maintainer-described testing and CI workflows have not been independently run. |
| [Kiln](https://github.com/instruktlabs/kiln) | Create editable procedural 3D assets with an agent, review rendered views and export GLB. | MIT; local MCP/CLI requires Node.js. Maintainer-described validation has not been independently tested; check licenses for downloaded packs. |
| [Godot Create 3D Assets](https://github.com/LuigiDeFacci/godot-create-3d-assets) | Build reusable Godot-native 3D scenes and inspect traversal, interaction and multi-angle screenshots. | MIT; requires Godot, Python and the described MCP setup. Maintainer-reported workflow has not been independently run. |
| [Godogen](https://github.com/htdt/godogen) | Scaffold a game project for Claude Code or Codex, with multi-engine instructions and a local asset-generation option. | MIT; engine and platform requirements vary. Its documented local asset route requires NVIDIA hardware; external services may incur costs. Not independently run. |
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


## 简体中文

这些是通用资源，不一定使用了 Fable 5.2。来源链接与下文记载的限制核查于 2026 年 11 月 12 日（UTC+8）；使用前请核对当前访问条件和条款。

### Agent Skills

| 资源 | 适合做什么 | 说明 |
| --- | --- | --- |
| [Blender Skills](https://github.com/EL4CTEO/blender-skills) | 查找 Blender 建模、绑定、材质、优化与导出技能。 | MIT；需要 Blender，可选连接 MCP。维护者所述测试尚未独立运行。 |
| [Open Game Skills](https://github.com/jammyfu/open-game-skills) | 查找游戏手感、镜头、战斗及引擎实现相关技能。 | MIT；Python 和目标引擎要求因技能而异。维护者说明 CI 不能证明智能体路由或游戏可玩性；尚未独立运行。 |
| [BlenderXAlpha 3DGenSkill](https://github.com/ig-shadow-walker/BlenderXAlpha-3DGenSkill) | 通过支持的生成服务在 Blender 中生成并放置 3D 资产。 | MIT；可能需要 Blender MCP、服务账号和额度。使用前阅读技能中的费用与确认步骤；尚未独立运行。 |
| [Godot Stagehand](https://github.com/mrf/godot-stagehand) · [Skill](https://github.com/mrf/godot-stagehand/blob/main/integrations/claude-code/skills/stagehand/SKILL.md) | 本地或在 CI 中运行 Godot 试玩场景、输入回放和截图比较。 | MIT；1.0 前版本，需要配置 Godot 插件及工具。维护者描述的功能尚未独立测试。 |
| [游戏发布技能](https://github.com/ericrisco/rsc-harness/blob/main/skills/gamedev-shipping/SKILL.md) | 参考不同引擎的构建、签名和发布流程。 | 所属仓库为 MIT；平台账号与工具链要求不同。版本化说明可能过时，应核对平台最新文档；尚未独立运行。 |
| [Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 参考基于 Remotion 的产品影片分镜及可编辑视频工作流。 | 仓库为 Apache-2.0，需要 Node、FFmpeg 及可选工具。分别核对 Remotion 和素材许可；尚未独立运行。 |
| [image-blaster](https://github.com/neilsonnn/image-blaster) · [作者 X 演示](https://x.com/neilsonks/status/2055013782771134479) | 了解 Claude Skill 工作流：将一张参考图拆分为静态世界、物体网格和音效。 | 仓库为 MIT；文档流程使用 Claude、World Labs 和 FAL，服务费用和产物权利依服务而异。未独立运行；X 原帖返回 403。 |
| [Codex GameDev Kit](https://github.com/IlyasGameDev/codex-gamedev-kit) | 查找面向 Unity、Godot 和 Unreal 的游戏开发技能与角色。 | MIT；面向 OpenAI Codex，需要相应引擎与工具配置。维护者的能力说明及工作流尚未独立测试。 |
| [Makone](https://github.com/wormholeportal/Makone) | 使用智能体流程制作程序化 Three.js 世界，并结合截图审查和浏览器检查。 | MIT；仓库介绍了集成运行环境、示例与验证工具，尚未独立运行。 |
| [Gua](https://github.com/gua-project/gua) | 通过语义场景检查、输入、录制和 MCP 自动化 Godot 与 Unity 试玩测试。 | MIT；需要受支持的引擎配置。维护者描述的测试和 CI 流程尚未独立运行。 |
| [Kiln](https://github.com/instruktlabs/kiln) | 配合智能体创建可编辑的程序化 3D 资产，审查渲染视图并导出 GLB。 | MIT；本地 MCP／命令行工具需要 Node.js。维护者描述的验证流程尚未独立测试；下载素材包需分别核对许可。 |
| [Godot Create 3D Assets](https://github.com/LuigiDeFacci/godot-create-3d-assets) | 在 Godot 内构建可复用的 3D 场景，并检查通行、交互与多角度截图。 | MIT；需要 Godot、Python 和文档中的 MCP 配置。维护者描述的流程尚未独立运行。 |
| [Godogen](https://github.com/htdt/godogen) | 为 Claude Code 或 Codex 创建游戏项目，提供多引擎指引及本地资产生成选项。 | MIT；引擎及系统要求各异。文档中的本地资产生成需要 NVIDIA 硬件，外部服务可能收费；尚未独立运行。 |
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

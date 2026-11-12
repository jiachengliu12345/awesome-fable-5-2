# Tutorials and creator workflows / 教程与创作经验

[Resource directory / 资源目录](../RESOURCES.md)

[English](#english) | [简体中文](#简体中文)

## English

These general resources are not necessarily Fable 5.2 examples. Source links and the limitations below were checked on 12 November 2026 (UTC+8); verify current access and terms before use.

### Reddit: workflows and critiques

<details>
<summary>Show Reddit: workflows and critiques</summary>

| Source | Practical takeaways | Scope and limits |
| --- | --- | --- |
| [Sketch, annotate, render, repeat](https://www.reddit.com/r/aigamedev/comments/1x8x7v2/a_nice_workflow_for_generating_basic_3d_assets_i/) · u/HuWeiliu | Send a sketch to a local queue, inspect the Blender render, draw changes over it and repeat. | Individual workflow using Claude and Blender; the creator says simple static assets work better than animals, which need more iterations. Specific model not stated. |
| [Six weeks building a cozy game](https://www.reddit.com/r/ClaudeAI/comments/1x721px/week_6_update_using_ai_to_build_a_game_with_no/) · u/Gambo7592 | Compare a 2D-reference → Meshy → Blender cleanup/rigging → Unity workflow with repeated human review. | Ongoing project; creator reports Opus 5.5, Sonnet, Gemini and Meshy as well as automated tests. Results and test coverage are not independently verified. |
| [ASCII shader readability in motion](https://www.reddit.com/r/TopologyAI/comments/1xf97z3/made_this_whole_thing_with_claude_code/) · u/czioscerny | Check whether a visual style stays readable during gameplay, not only in a still image. | One creator reports dropping the effect from a game because motion was hard to read and retaining it for an animation. No reusable prompt was provided. |
| [Animated island with Claude Code and img2threejs](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/) · u/Quirky_Success8287 | Use a reference and separate prop sheet; review props individually; simplify larger imported meshes and rebake normal maps; keep a boat synchronized with the water's wave function. | Creator-reported workflow and measurements; the scoring threshold is the creator's own. Model version not specified in the post. |
| [Code-generated walkable street](https://www.reddit.com/r/TopologyAI/comments/1vobf1y/an_llm_generated_this_complete_3d_scene_in_the/) · u/Certain_Friendship16 | The post links [source and five prompts](https://github.com/StarKnightt/night-street). Comments question whether building and vehicle geometry makes sense up close; inspect geometry rather than judging only a moving preview. | Claude and Three.js/R3F; specific Claude version not stated in the post. Useful as a prototype and critique, not evidence of production quality. |
| [3D roguelite: three sessions and a playtest](https://www.reddit.com/r/aigamedev/comments/1vjv3z8/i_left_claude_code_running_for_24h_it_built_a_3d/) · u/victorrseloy2 | The creator describes a base build, a follow-up after a real playtest, then a finishing session; the post links the original prompt and describes a deterministic frame-by-frame trailer. | Creator says Opus 5, existing Kenney/KayKit assets and generated audio were also used. It was not a single uninterrupted prompt; performance and cost are author reports. |
| [Browser FPS with code-generated models](https://www.reddit.com/r/ClaudeAI/comments/1x8dg94/i_made_a_browser_fps_with_claude_code_every_3d/) · u/Inevitable_Salad_128 | The creator iterated a Three.js FPS over about a month and generated models in code; the discussion considers mobile, controller support and alternative asset pipelines. | Creator names Opus 5.5 and Sonnet 5.5, not Fable 5.2. Other commenters' pipelines are their own, not the author's. |
| [Image-to-3D reference and rebuild workflow](https://www.reddit.com/r/aigamedev/comments/1xa3gju/new_crazy_workflow_for_making_3d_assets/) · u/FearlessCounty3487 and u/mr_undeadpickle77 | The original poster describes importing a generated rough model into Godot and rebuilding it; a commenter documented a separate Meshy → Godot → interactive preview workflow and published a skill. | Both are individual accounts. The commenter names Opus 5.5, GPT Image 2.5 and Meshy 7; generated assets and services have their own terms. |

</details>

### X and developer tutorials

<details>
<summary>Show X and developer tutorials</summary>

| Source | Practical use | Scope and limits |
| --- | --- | --- |
| [PlayCanvas: make a game](https://developer.playcanvas.com/tutorials/crash-course/) | Follow a browser game tutorial covering entities, scripts, physics, animation and events. | Official PlayCanvas material; the page states that the polish-and-publish stage is not yet complete. |
| [Unreal Engine: procedural content generation](https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-in-unreal-engine) | Explore procedural asset placement, biomes and world-building tools, with links to GPU and runtime-debugging guidance. | Epic's engine-specific documentation; not an AI-model demonstration. |
| [Babylon.js: procedural textures](https://doc.babylonjs.com/features/featuresDeepDive/materials/advanced/custom_procedural_textures/) | Study configurable GPU-generated textures for browser scenes. | Official Babylon.js documentation; requires familiarity with shaders and the engine. |
| [Three.js: textures](https://threejs.org/manual/pages/textures.html) | Understand texture loading, filtering and GPU memory when optimizing interactive scenes. | General rendering guidance; actual memory and performance depend on device and asset settings. |
| [Tripo: Vibe Gaming Playbook](https://www.tripo3d.ai/tutorials/vibe-gaming) | Work through a staged Three.js browser-game workflow: playable greybox, asset list, model replacement and device checks. | Vendor playbook uses Claude Code or Codex and Tripo Studio; generated assets and features depend on the plan and terms. Not independently run. |
| [Sunny Valley Studio on X: Claude Code + Unity MCP 3D platformer](https://x.com/SunnyVStudio/status/2061879369950282060) · [linked tutorial](https://youtu.be/gSFHyso_uuI) | Entry point to a Unity 3D platformer prototyping tutorial. | The post text was visible in search; X returned 403 and the video was throttled when checked. Detailed steps and model version were not independently verified. |
| [Meta Model API: one-shot game dev](https://dev.meta.ai/docs/cookbook/one-shot-game-dev) | Study a structured Three.js game prompt with explicit coordinates, collision and moving-platform rules. | Vendor example uses Muse Spark and OpenCode; no iterative repair or evaluation harness is described. Results vary and were not independently reproduced. |
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

</details>

For community feedback on the catalog's works, see [Community Feedback & Trends](../COMMUNITY-FEEDBACK.md#english). Search and access limitations for the case collection are in the [search log](../SEARCH-LOG.md).


## 简体中文

这些是通用资源，不一定使用了 Fable 5.2。来源链接与下文记载的限制核查于 2026 年 11 月 12 日（UTC+8）；使用前请核对当前访问条件和条款。

### Reddit：工作流与反面意见

<details>
<summary>展开 Reddit：工作流与反面意见</summary>

| 来源 | 值得参考的做法 | 适用范围与限制 |
| --- | --- | --- |
| [草图批注与渲染迭代](https://www.reddit.com/r/aigamedev/comments/1x8x7v2/a_nice_workflow_for_generating_basic_3d_assets_i/) · u/HuWeiliu | 将草图交给本地队列，查看 Blender 渲染图，再直接画出修改意见并重复。 | 使用 Claude 和 Blender 的个人流程；作者称简单静态资产效果较好，动物需要更多轮迭代。帖子未说明具体模型。 |
| [六周制作治愈系游戏](https://www.reddit.com/r/ClaudeAI/comments/1x721px/week_6_update_using_ai_to_build_a_game_with_no/) · u/Gambo7592 | 参考“二维设定图 → Meshy → Blender 清理和绑定 → Unity”的流程，并反复由人审查。 | 项目仍在制作；作者自述使用 Opus 5.5、Sonnet、Gemini 和 Meshy，也使用自动化测试。效果与测试覆盖未经独立核验。 |
| [ASCII 着色器的动态可读性](https://www.reddit.com/r/TopologyAI/comments/1xf97z3/made_this_whole_thing_with_claude_code/) · u/czioscerny | 检查视觉风格在游戏运动过程中是否仍然清晰。 | 一位创作者称动态画面难以辨认，因此放弃用于游戏，改为保留动画实验；未提供可复用提示词。 |
| [用 Claude Code 和 img2threejs 制作动态岛屿](https://www.reddit.com/r/threejs/comments/1x9ze32/i_built_an_animated_3d_island_with_claude_code/) · u/Quirky_Success8287 | 准备参考图和分物件素材图，逐项检查小道具；简化较大的导入模型后重新烘焙法线贴图；让船与海水使用同一套波浪函数。 | 流程和性能数字来自作者自述；评分门槛是作者自己的选择。帖子未注明具体模型版本。 |
| [纯代码生成的可漫游街景](https://www.reddit.com/r/TopologyAI/comments/1vobf1y/an_llm_generated_this_complete_3d_scene_in_the/) · u/Certain_Friendship16 | 帖子链接了[源码和五条提示词](https://github.com/StarKnightt/night-street)。评论者指出建筑和车辆的局部结构可能不合理，提醒我们近距离检查几何，而不仅看移动镜头。 | 使用 Claude 和 Three.js/R3F；帖子未注明 Claude 具体版本。适合作为原型与批评案例，不代表达到产品级质量。 |
| [3D Roguelite：分三次构建并穿插试玩](https://www.reddit.com/r/aigamedev/comments/1vjv3z8/i_left_claude_code_running_for_24h_it_built_a_3d/) · u/victorrseloy2 | 作者描述先做基础版本、实际试玩后继续迭代，再做收尾；帖子提供原始提示词，并介绍逐帧生成预告片的方法。 | 作者称使用 Opus 5，也使用了现成 Kenney/KayKit 资产和生成音频；并非单次不间断提示。性能与成本为作者自述。 |
| [浏览器 FPS：模型由代码生成](https://www.reddit.com/r/ClaudeAI/comments/1x8dg94/i_made_a_browser_fps_with_claude_code_every_3d/) · u/Inevitable_Salad_128 | 作者用约一个月迭代 Three.js FPS，直接用代码生成模型；讨论还涉及手机、手柄和其他资产制作流程。 | 作者提及 Opus 5.5 和 Sonnet 5.5，而非 Fable 5.2。其他评论者的资产管线属于其个人经验，不应归给原作者。 |
| [用图生粗模作参考，再重建 3D 资产](https://www.reddit.com/r/aigamedev/comments/1xa3gju/new_crazy_workflow_for_making_3d_assets/) · u/FearlessCounty3487 与 u/mr_undeadpickle77 | 原帖作者介绍先把生成粗模导入 Godot 再重建；另一位评论者记录了自己的 Meshy → Godot → 交互预览流程，并发布了对应 Skill。 | 均为个人经验；评论者注明使用 Opus 5.5、GPT Image 2.5 和 Meshy 7。生成资产及服务需分别核对条款。 |

</details>

### X 与开发者教程

<details>
<summary>展开 X 与开发者教程</summary>

| 来源 | 值得参考的内容 | 适用范围与限制 |
| --- | --- | --- |
| [PlayCanvas：制作游戏入门](https://developer.playcanvas.com/tutorials/crash-course/) | 按浏览器游戏教程学习实体、脚本、物理、动画和事件。 | PlayCanvas 官方资料；页面注明润色与发布阶段尚未完成。 |
| [Unreal Engine：程序化内容生成](https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-in-unreal-engine) | 了解程序化资产布局、生态群系和世界构建，并查阅 GPU 与运行时调试指南。 | Epic 的引擎文档，并非 AI 模型演示。 |
| [Babylon.js：程序化纹理](https://doc.babylonjs.com/features/featuresDeepDive/materials/advanced/custom_procedural_textures/) | 学习为浏览器场景配置 GPU 生成的纹理。 | Babylon.js 官方文档，需要了解着色器和引擎。 |
| [Three.js：纹理](https://threejs.org/manual/pages/textures.html) | 了解纹理加载、过滤和显存占用，辅助优化交互场景。 | 通用渲染资料；实际显存和性能取决于设备及资产设置。 |
| [Tripo：Vibe Gaming 制作指南](https://www.tripo3d.ai/tutorials/vibe-gaming) | 分阶段制作 Three.js 浏览器游戏：可玩的灰盒、资产清单、模型替换和设备检查。 | 厂商指南使用 Claude Code 或 Codex 与 Tripo Studio；生成资产和功能受方案及条款约束。尚未独立运行。 |
| [Sunny Valley Studio 的 X 帖：Claude Code + Unity MCP 制作 3D 平台游戏](https://x.com/SunnyVStudio/status/2061879369950282060) · [关联教程](https://youtu.be/gSFHyso_uuI) | 使用 Unity 快速制作 3D 平台游戏原型的教程入口。 | 搜索结果可见帖子文字；检查时 X 返回 403，视频被限流，具体步骤和模型版本未能独立核实。 |
| [Meta Model API：单次生成游戏](https://dev.meta.ai/docs/cookbook/one-shot-game-dev) | 研究 Three.js 游戏提示词中如何明确坐标、碰撞和移动平台规则。 | 厂商示例使用 Muse Spark 与 OpenCode；未采用迭代修复或评测工具。生成结果会变化，尚未独立复现。 |
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

</details>

案例库内的作品反馈见[社区反馈与趋势](../COMMUNITY-FEEDBACK.md#简体中文)；案例检索与访问限制见[检索记录](../SEARCH-LOG.md)。

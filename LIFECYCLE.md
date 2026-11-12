# Making and maintaining 3D creations / 3D 作品制作与维护

[English](#english) | [简体中文](#简体中文)

## English

A practical companion to the [case catalog](README.md) and [resource directory](RESOURCES.md), organized around what a creator needs next. Sources checked on 12 November 2026 (UTC+8); see the [search log](LIFECYCLE-SEARCH-LOG.md). Fable-specific examples are **creator reports**, not independently reproduced runs. Engineering documentation is general and does not imply that a particular Fable project used it. A link is not an endorsement; check availability, costs and the terms of each tool and asset. Reddit originals were readable through a web index, while direct automated requests returned 403; access may vary.

### 1. Brief, build and iterate

<details>
<summary>Show: 1. Brief, build and iterate</summary>


- **[Tria Prima](https://www.reddit.com/r/vibecoding/comments/1xsslew/created_a_dark_fantasy_game_with_fable_52_one/)** · [Code](https://github.com/winchxyz/tria-prima) · [Play](https://winchxyz.github.io/tria-prima/). The creator published the initial brief, describes changing the art direction mid-build and fixing three bugs after playing, and reports 4 hours for the first build and 6.5 hours including fixes. An existing catalog work; timings and quality are self-reported, not a guaranteed recipe.
- **[Matrix city: creator's iteration](https://www.reddit.com/r/ClaudeAI/comments/1xtdqcr/follow_the_white_rabbit_i_directed_claude_fable/)** · [Code](https://github.com/tornikegomareli/Matrix). A browser world developed across multiple rounds, with discussion of atmosphere and motion rather than a single prompt. The author reports roughly 22 hours and over 70 commits. This is additional workflow evidence for an existing catalog work; the full conversation is not provided.
- **[Graveyard Shift](https://www.reddit.com/r/threejs/comments/1xtvxx0/i_asked_claude_fable_52_to_make_a_cod_zombies/)** · [Code and setup](https://github.com/ethanplusai/zombies) · [Play](https://zombies.ethanplus.ai/). Three.js zombie shooter with runnable source and setup instructions. The creator reports about 14 hours with Fable 5.2 and Sonnet 5.5 / Opus 5.5 subprocesses. The original prompt was not found; the creator's claim has not been independently reproduced. The repository states MIT; verify terms for the version used.
- **[Paper-plane game brief and comparison](https://www.reddit.com/r/codex/comments/1xtgbs7/same_game_prompt_no_testing_allowed_gpt61_sol/)** · [Recorded outputs](https://evals.ag/tasks/tsk_49SD3AKJN4T0E2YR715N6D9CWA). The author shares a complete brief describing controls, a two-minute loop and an ending. Fable 5.2 is one of four outputs. One run per model used different agent harnesses, and the prompt forbids testing: useful as a brief example, not a controlled benchmark or recommended release process.

- **[Yonkers Rises](https://simonwillison.net/2026/Nov/10/yonkers-rises/)** · [Animation](https://tools.simonwillison.net/yonkers-rises). Simon Willison shares his original Three.js / OpenStreetMap brief and says he used Fable 5.2 Medium. The delivered page has readable client code; no runtime or cost is reported.
- **[The Edge: production breakdown](https://x.com/rileybrown/status/2119902109709537708)** · [Making-of artifact](https://claude.ai/artifact/QGWUAjRrzRzZWGcQzSMLfa). The creator describes a Fable-built Blender film with 13 shots and rented-GPU rendering; the reported render bill does not include all model or audio-service costs. The artifact was inaccessible in this check and the complete project was not verified.


</details>

### 2. Playtest and repair

<details>
<summary>Show: 2. Playtest and repair</summary>


- **[Fable-assisted game-mod test](https://www.reddit.com/r/Anthropic/comments/1xsht0d/my_fable_52_spent_75_hours_in_goal_mode_last/)**. A creator describes a separate tester using game-state tools, sending bug reports to development sessions and rechecking fixes. One reported issue was later rejected as a false alarm. The reported counts are self-reported; this is a mod for an existing game, not a generated standalone game.
- **[Playwright device emulation](https://playwright.dev/docs/emulation)** · [Visual comparisons](https://playwright.dev/docs/test-snapshots) · [Trace viewer](https://playwright.dev/docs/trace-viewer). Check inputs, page states and visual changes, then inspect screenshots, network and console. Device emulation is not a substitute for testing a real phone or GPU; screenshot baselines depend on the rendering environment. Canvas images alone do not establish gameplay quality.
- **[Android remote debugging](https://developer.chrome.com/docs/devtools/remote-debugging)**. Inspect a real Android Chrome session from a computer. The documentation warns that screencasting affects frame rate; turn it off when measuring performance.

- **[Accessibility Insights for Web](https://accessibilityinsights.io/docs/web/overview/)**. Check HTML menus and controls with automated rules and assisted keyboard inspection. Canvas content, gamepad access and the experience itself require additional testing; the tool was not run here.


</details>

### 3. Assets, rendering and performance

<details>
<summary>Show: 3. Assets, rendering and performance</summary>


- **[Fable-assisted PBR materials](https://www.reddit.com/r/TopologyAI/comments/1xu2m3j/from_prompt_to_seamless_ai_pbr_material_in_under/)**. The author describes concept previews, image-generated color and height maps, Python-derived maps, and Blender/Cycles renders. Image generation and Poly Haven assets were also used; reported image costs exclude agent tokens. Individual results and rights were not independently checked.
- **[glTF Validator](https://github.com/KhronosGroup/glTF-Validator)** · [Browser version](https://github.khronos.org/glTF-Validator/). Check GLB/glTF structure and examine a validation report before importing assets. Browser validation runs locally; a valid file is not necessarily visually correct or licensed for a use.
- **[glTF Sample Viewer](https://github.com/KhronosGroup/glTF-Sample-Viewer)** · [glTF Transform CLI](https://gltf-transform.dev/cli). Inspect assets in a viewer and investigate or optimize geometry and textures; compare appearance and compatibility after changes. Tool capabilities are documented by their maintainers and not tested here.
- **[Spector.js](https://github.com/BabylonJS/Spector.js)** · [Three.js renderer information](https://threejs.org/docs/pages/WebGLRenderer.html) · [Resource disposal](https://threejs.org/manual/pages/how-to-dispose-of-objects.html). Inspect WebGL commands, draw calls and resource use, and dispose of unused Three.js resources when appropriate. Spector is a WebGL debugging tool, not a gameplay test.

- **[PlayCanvas Inspector Performance](https://developer.playcanvas.com/user-manual/optimization/inspector-performance/)**. Inspect frame-by-frame CPU, optional GPU timing, loading and draw-call statistics for a PlayCanvas application; detailed profiling requires an appropriate build. The vendor documentation was checked, not the tool run.

- **[FMOD Studio](https://www.fmod.com/studio)** · [Profiler](https://www.fmod.com/docs/2.04/studio/profiling.html). Create and profile interactive game audio with an engine integration. It is commercial software with eligibility-based terms; check the [current licensing](https://www.fmod.com/licensing) and project requirements. Not independently run.

- **[Unreal Insights](https://dev.epicgames.com/documentation/unreal-engine/unreal-insights-in-unreal-engine)**. Trace and inspect performance in Unreal Engine projects. Results depend on capture configuration and target hardware; not independently run.

- **[Roman building asset workflow](https://www.reddit.com/r/ClaudeCode/comments/1xsh2bq/fable_52_roman_buildings/)**. The creator describes Fable 5.2 generating Blender scripts, rendering exported models from game-camera views, checking LODs and reviewing screenshots. The process and results are self-reported; historical accuracy was not reviewed by a historian.


</details>

### 4. Publish and maintain

<details>
<summary>Show: 4. Publish and maintain</summary>


- **[Cloudflare Pages Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)**. Connect a repository for builds, deploys and previews. Check the provider's limitations before choosing a deployment method; the documentation notes that an existing Git-integrated Pages project cannot be switched to Direct Upload.
- **[Workers metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/)** · [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/). For a deployment using Workers, inspect service-side errors and logs after release. These do not measure a player's GPU frame rate; review the current limits and pricing.
- **[Service worker guide](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)**. If an experience needs offline caching, plan cache updates and test new releases with existing browser storage. Offline support is optional and adds maintenance work.

- **[itch.io butler](https://itch.io/docs/butler/pushing.html)**. Upload and update builds on release channels, transferring changes on later uploads. Requires an itch.io account and project; review platform terms and costs separately.

- **[SteamPipe](https://partner.steamgames.com/doc/sdk/uploading)**. Upload and test builds for Steam using Steamworks; requires an eligible app and account. Platform-specific; check current distribution terms.
- **[Sentry JavaScript](https://sentry.io/for/javascript/)** · [Session Replay](https://sentry.io/product/session-replay/). Investigate client errors and browser interaction records after release. Requires SDK configuration and an account; configure privacy, sampling and cost limits. WebGL canvas replay was not verified.


</details>

### 5. Code-driven film and animation

<details>
<summary>Show: 5. Code-driven film and animation</summary>


- **[Blender scene and procedural spider](https://www.reddit.com/r/ClaudeAI/comments/1xu4r5m/fable_52_built_this_scene_in_blender/)**. The author credits Fable 5.2 for the Blender scene and describes GPT reference images, Tripo models, procedural walking, scripted sound and a rented-GPU render. The post does not provide the project files; this is a workflow report, not a reproducible project.
- **[Treehouse film setup](https://nanoflow.blog/guides/one-prompt-treehouse-film-setup-guide)**. The author describes a Fable 5.2 / Blender workflow with a shared event timeline, draft render and resumable final chunks. Only the opening section is accessible without signup; the full prompt and guide were not reviewed. Hardware and external audio services are involved.
- **[Remotion rendering guide](https://www.remotion.dev/docs/render)**. Extend the already-listed Remotion skills with practical options for rendering code-driven video. This is a general tool; check Remotion's license and pricing for the intended use.

- **[Blender Flamenco](https://flamenco.blender.org/)** · [Quickstart](https://flamenco.blender.org/usage/quickstart/). Schedule Blender frame rendering over self-managed workers and assemble previews. Requires Blender, a manager, workers and shared storage; it does not split a single frame across workers. Infrastructure and compute can cost money. Not independently run.

- **[Mineral Zone trailer workflow](https://www.reddit.com/r/ClaudeGameDev/comments/1xs4owt/fable_52_filmed_and_edited_my_games_trailer_by/)**. The creator describes Fable 5.2 capturing and editing a Godot game trailer using a scripted capture scene, existing saves, music and iterative feedback. The author says the agent could not check how the audio sounded. The setup and outcome are self-reported and not independently reproduced.

- **[Prompt-to-video tutorial](https://github.com/sandbase-lab/awesome-fable-5-2/blob/main/docs/tutorial.md)**. A provider explains a prompt → generated HTML → browser recording → MP4 workflow, including its own API and arena. Requires accounts or services for some steps; not independently reproduced.


</details>

### 6. Record enough to reproduce

<details>
<summary>Show: 6. Record enough to reproduce</summary>


When a creator has actually shared them, preserve links to the original brief, model and tool versions, source revision, setup commands, asset origins, runtime requirements, playtest observations and costs. Mark omissions as unknown. Distinguish a browser-delivered build from the full authoring project, and distinguish source access from reuse rights. The existing [code audit](CODE-AUDIT.md) remains the authority for the catalog's verification status; this companion does not change its count.


</details>

## 简体中文

这份指南是[案例库](README.zh-CN.md)和[资源目录](RESOURCES.md#简体中文)的实用补充，按创作者下一步要解决的问题组织。来源核查日期为 2026 年 11 月 12 日（UTC+8）；过程见[检索记录](LIFECYCLE-SEARCH-LOG.md)。Fable 案例中的运行过程和数字来自**创作者自述**，我们没有独立复现；通用工程文档不代表某个 Fable 项目实际使用过该工具。链接不等于推荐背书，使用前请检查工具和素材各自的费用与条款。Reddit 原帖可通过网页索引读取，但直接自动化请求返回 403；实际访问情况可能不同。

### 1. 写清目标、制作与迭代

<details>
<summary>展开：1. 写清目标、制作与迭代</summary>


- **[Tria Prima](https://www.reddit.com/r/vibecoding/comments/1xsslew/created_a_dark_fantasy_game_with_fable_52_one/)** · [代码](https://github.com/winchxyz/tria-prima) · [试玩](https://winchxyz.github.io/tria-prima/)。作者公开了初始需求，描述中途调整美术方向、试玩后修复三个问题，并称初版用了 4 小时、加修复共 6.5 小时。作品已在案例库；耗时和效果是个人报告，并非保证可以复现。
- **[Matrix 城市：作者的迭代记录](https://www.reddit.com/r/ClaudeAI/comments/1xtdqcr/follow_the_white_rabbit_i_directed_claude_fable/)** · [代码](https://github.com/tornikegomareli/Matrix)。浏览器世界经过多轮修改，作者讨论了氛围和动态表现，称耗时约 22 小时、提交超过 70 次。这是已有案例的补充工作流资料；完整对话未公开。
- **[Graveyard Shift](https://www.reddit.com/r/threejs/comments/1xtvxx0/i_asked_claude_fable_52_to_make_a_cod_zombies/)** · [代码与运行说明](https://github.com/ethanplusai/zombies) · [试玩](https://zombies.ethanplus.ai/)。Three.js 僵尸射击游戏，提供源码和运行说明。作者称制作约 14 小时，主要使用 Fable 5.2，子流程还用了 Sonnet 5.5 和 Opus 5.5。未找到原始提示词，也未独立复现；仓库标注 MIT，使用时请核对对应版本的条款。
- **[纸飞机游戏简报与对比](https://www.reddit.com/r/codex/comments/1xtgbs7/same_game_prompt_no_testing_allowed_gpt61_sol/)** · [运行结果](https://evals.ag/tasks/tsk_49SD3AKJN4T0E2YR715N6D9CWA)。作者公开了完整简报，包含操作、两分钟的玩法循环和结尾；Fable 5.2 是四个输出之一。每个模型只运行一次，使用的智能体环境不同，且提示词禁止测试：适合参考如何写需求，不能作为严格基准或建议的发布流程。

- **[Yonkers Rises](https://simonwillison.net/2026/Nov/10/yonkers-rises/)** · [观看动画](https://tools.simonwillison.net/yonkers-rises)。Simon Willison 分享了原始 Three.js 与 OpenStreetMap 提示词，并称使用 Fable 5.2 Medium。网页交付的客户端代码可读；作者未给出耗时或费用。
- **[The Edge：制作解析](https://x.com/rileybrown/status/2119902109709537708)** · [制作说明 Artifact](https://claude.ai/artifact/QGWUAjRrzRzZWGcQzSMLfa)。作者介绍了一部由 Fable 构建的 Blender 影片，包含 13 个镜头，并使用租用 GPU 渲染；所报渲染费不等于模型及音频服务的总成本。本次检查无法访问该 Artifact，完整工程也未核实。


</details>

### 2. 试玩与修复

<details>
<summary>展开：2. 试玩与修复</summary>


- **[用 Fable 辅助测试游戏模组](https://www.reddit.com/r/Anthropic/comments/1xsht0d/my_fable_52_spent_75_hours_in_goal_mode_last/)**。作者描述了测试会话读取游戏状态、向开发会话报告问题并复测修复的过程，其中一条报告后来被排除为误报。测试数字来自作者自述；这是现有游戏的模组，并非从零生成的独立游戏。
- **[Playwright 设备模拟](https://playwright.dev/docs/emulation)** · [截图比较](https://playwright.dev/docs/test-snapshots) · [操作追踪](https://playwright.dev/docs/trace-viewer)。可检查输入、页面状态和画面变化，再查看截图、网络与控制台。设备模拟不能代替真实手机或 GPU 测试；截图基线受渲染环境影响，Canvas 图片也不能单独证明玩法质量。
- **[Android 真机远程调试](https://developer.chrome.com/docs/devtools/remote-debugging)**。通过电脑检查真实 Android Chrome 会话。官方文档提示屏幕投射会影响帧率，测性能时应关闭。

- **[Accessibility Insights for Web](https://accessibilityinsights.io/docs/web/overview/)**。对 HTML 菜单和控件进行自动规则与辅助键盘检查；Canvas 内容、手柄和实际体验仍需其他测试。本项目未独立运行该工具。


</details>

### 3. 资产、渲染与性能

<details>
<summary>展开：3. 资产、渲染与性能</summary>


- **[Fable 辅助制作 PBR 材质](https://www.reddit.com/r/TopologyAI/comments/1xu2m3j/from_prompt_to_seamless_ai_pbr_material_in_under/)**。作者介绍了概念预览、图像生成颜色和高度图、Python 衍生贴图及 Blender/Cycles 渲染；流程还用了图像生成服务和 Poly Haven 素材，所报图像费用不含智能体 token。结果与使用权未独立核实。
- **[glTF Validator](https://github.com/KhronosGroup/glTF-Validator)** · [浏览器版](https://github.khronos.org/glTF-Validator/)。导入前检查 GLB/glTF 文件结构并查看报告。浏览器版在本地验证；格式有效不代表画面正确或获得了使用授权。
- **[glTF Sample Viewer](https://github.com/KhronosGroup/glTF-Sample-Viewer)** · [glTF Transform 命令行](https://gltf-transform.dev/cli)。分别用于查看资产，以及检查或优化几何和纹理；修改后应比较画面和兼容性。能力说明来自维护者文档，本项目尚未运行测试。
- **[Spector.js](https://github.com/BabylonJS/Spector.js)** · [Three.js 渲染统计](https://threejs.org/docs/pages/WebGLRenderer.html) · [资源释放](https://threejs.org/manual/pages/how-to-dispose-of-objects.html)。检查 WebGL 调用、绘制次数和资源使用，并在适当时释放不再需要的 Three.js 资源。Spector 是渲染调试工具，不能替代玩法测试。

- **[PlayCanvas Inspector Performance](https://developer.playcanvas.com/user-manual/optimization/inspector-performance/)**。针对 PlayCanvas 项目逐帧检查 CPU、可选 GPU 时间、加载和绘制次数；更详细的分析需要合适的构建版本。已核对官方文档，未独立运行。

- **[FMOD Studio](https://www.fmod.com/studio)** · [性能分析器](https://www.fmod.com/docs/2.04/studio/profiling.html)。结合游戏引擎制作并检查互动音频；属于商业软件，不同项目适用的条款不同，应核对[当前许可](https://www.fmod.com/licensing)和项目要求。本项目未独立运行。

- **[Unreal Insights](https://dev.epicgames.com/documentation/unreal-engine/unreal-insights-in-unreal-engine)**。为 Unreal Engine 项目采集和分析性能追踪；结果受采集配置与目标设备影响，尚未独立运行。

- **[罗马建筑资产制作流程](https://www.reddit.com/r/ClaudeCode/comments/1xsh2bq/fable_52_roman_buildings/)**。作者介绍使用 Fable 5.2 编写 Blender 脚本，再按游戏镜头渲染导出模型、检查不同细节层级并审阅截图。流程与结果来自作者自述，历史准确性未经过历史学家审查。


</details>

### 4. 发布与维护

<details>
<summary>展开：4. 发布与维护</summary>


- **[Cloudflare Pages 的 Git 集成](https://developers.cloudflare.com/pages/get-started/git-integration/)**。连接代码仓库以构建、部署和预览。选择方式前应检查平台限制；官方说明现有 Git 集成项目不能直接切换为 Direct Upload。
- **[Workers 指标](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/)** · [Workers 日志](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)。适用于使用 Workers 的部署，帮助上线后查看服务端错误与日志；它们不能测玩家设备的 GPU 帧率，额度和价格以平台当前说明为准。
- **[Service Worker 指南](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)**。如果作品确实需要离线缓存，应规划缓存更新，并在已有浏览器数据的情况下测试新版本。离线功能是可选项，也会增加维护工作。

- **[itch.io butler](https://itch.io/docs/butler/pushing.html)**。向发布渠道上传并更新构建，后续上传可传输变化部分。需要 itch.io 账号和项目，平台条款及费用需另行核对。

- **[SteamPipe](https://partner.steamgames.com/doc/sdk/uploading)**。通过 Steamworks 上传和测试 Steam 构建；需要符合条件的应用与账号，发行条款以平台当前规定为准。
- **[Sentry JavaScript](https://sentry.io/for/javascript/)** · [会话回放](https://sentry.io/product/session-replay/)。上线后辅助排查客户端错误和浏览器交互记录；需要配置 SDK 与账号，并设置隐私、采样及费用限制。WebGL 画面回放能力未核实。


</details>

### 5. 代码影片与动画

<details>
<summary>展开：5. 代码影片与动画</summary>


- **[Blender 场景与程序化蜘蛛](https://www.reddit.com/r/ClaudeAI/comments/1xu4r5m/fable_52_built_this_scene_in_blender/)**。作者称使用 Fable 5.2 制作 Blender 场景，同时使用 GPT 参考图、Tripo 模型、程序化行走、脚本音效和租用 GPU 渲染。帖子未提供工程文件，属于流程分享，不能直接复现。
- **[树屋影片制作指南](https://nanoflow.blog/guides/one-prompt-treehouse-film-setup-guide)**。作者介绍 Fable 5.2 与 Blender 的流程，包括共享事件时间线、草稿渲染和可续传的最终分段渲染。无需注册只能阅读开头，完整提示词和教程未核查；流程涉及硬件与外部音频服务。
- **[Remotion 渲染指南](https://www.remotion.dev/docs/render)**。为现有 Remotion Skills 补充代码影片的实际渲染方法。这是通用工具，具体用途应核对 Remotion 的许可证和价格。

- **[Blender Flamenco](https://flamenco.blender.org/)** · [快速入门](https://flamenco.blender.org/usage/quickstart/)。使用自行管理的工作节点调度 Blender 逐帧渲染并合成预览，需要 Blender、管理器、工作节点和共享存储；不能把单帧分配给多个节点。基础设施和算力可能产生费用，尚未独立运行。

- **[Mineral Zone 预告片流程](https://www.reddit.com/r/ClaudeGameDev/comments/1xs4owt/fable_52_filmed_and_edited_my_games_trailer_by/)**。作者描述 Fable 5.2 利用 Godot 的脚本化录制场景、现有存档、音乐和多轮反馈制作游戏预告；作者也说智能体无法自行判断声音效果。流程和结果来自作者自述，尚未独立复现。

- **[从提示词到视频的教程](https://github.com/sandbase-lab/awesome-fable-5-2/blob/main/docs/tutorial.md)**。服务商介绍提示词 → 生成 HTML → 浏览器录制 → MP4 的流程，其中包含其自有 API 和竞技场；部分步骤需要账号或服务，尚未独立复现。


</details>

### 6. 留下可复现的信息

<details>
<summary>展开：6. 留下可复现的信息</summary>


创作者实际公开时，尽量保存原始需求、模型和工具版本、代码修订、安装命令、素材来源、运行条件、试玩问题与成本的链接；未公开的内容标为未知。区分浏览器交付文件与完整制作工程，也区分代码可访问和获得再使用许可。案例计数仍以现有[代码与模型证据核验](CODE-AUDIT.md#简体中文)为准；本指南不会更改该计数。


</details>

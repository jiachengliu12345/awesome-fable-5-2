# 3D assets as code / 代码构建的 3D 资产

[English](#english) | [简体中文](#简体中文)

## English

A selection of editable code, procedural generators and research datasets for 3D objects. These are **general 3D resources**, not claims of Fable 5.2 use. Sources were checked on 12 November 2026 (UTC+8); see the [search log](CODE-ASSET-SEARCH-LOG.md). Projects and assets were not independently run or rendered. Check the license of each codebase, dataset, third-party asset and output separately.

### Open-source, commercial-use code and node assets

These licenses permit commercial use of the cited project code or assets under their terms; check separate third-party assets and outputs where noted. Nothing here was independently run.

| Resource | Editable material | License and practical notes |
| --- | --- | --- |
| [ModKit](https://github.com/JaronKBragg7337/asset-pack-ue-threejs-blender-unity) | Procedurally generated modular buildings and props, with Blender source, scripts and GLB/FBX exports. | Project declares meshes, scripts and renders CC0-1.0; inspect any third-party content separately. |
| [NeuralStock](https://github.com/Neuralstock/neuralstock) | Room Zero collection of Blender source, procedural generators and GLB assets for assembling rooms. | Repository software MIT; published asset content CC0-1.0 according to its asset policy. Provenance and validation are maintainer-reported; verify the rights for each release. |
| [CGFigures Asset Library](https://www.cgfigures.ca/assetlibrary) | Blender Asset Browser library for scientific visualization, including editable models and node tools. | CC0 1.0 per its creator; free and paid editions are described as identical. Download contents were not independently inspected. |
| [RFX Blender Asset Library](https://github.com/Pixelguru26/RFX-Blender-Asset-Library) | Blender geometry nodes, modifiers, materials and textures, including hard-surface and science-fiction tools. | CC0-1.0; the maintainer permits use, modification and redistribution. Some assets are work in progress. |
| [Primitive Assets Library](https://github.com/pesaksintondji/primitive-assets-library) | Blender Geometry Nodes primitives and hard-surface parts, with a Python script to rebuild the library. | Assets and scripts CC0-1.0; requires a compatible Blender version. |
| [Geometry Node Asset Files](https://github.com/johnnygizmo/node_assets) | Editable Blender `.blend` node groups for use in the Asset Browser. | CC0-1.0. The maintainer says the files were created with Blender daily builds; check version compatibility. |
| [Procedural 3D assets](https://github.com/boytchev/3d-assets) | Three.js source for individually editable procedural objects. | Repository MIT; retain the copyright and license notice when redistributing code. Check any separate content and output rights. |
| [Cosmo Tree Gen](https://github.com/FrogCosmonaut/cosmo_tree_gen) | Godot tree generator with editable parameters, presets, LOD and GLB/glTF export. | MIT code; requires Godot 4.6+. The project credits CC0 leaf textures and ambientCG bark; check the included third-party notices. |
| [SimpleXTerrain](https://github.com/prajwal-mx/SimpleXTerrain) | Godot node-graph terrain generator with editable biome, noise and erosion rules. | MIT code; requires Godot .NET and Terrain3D. It generates terrain inside the engine, not a standalone model pack. |
| [Godot Road Generator](https://github.com/TheDuckCow/godot-road-generator) | Parametric roads, intersections and lanes with editable Godot source and glTF export. | MIT code; Godot 4.4+. Review the project and third-party notices for bundled assets. |
| [TreeForge](https://github.com/Kapilthakur1520/treeforge) | Parameterized procedural tree generation for visualization and 3D assets. | MIT code, including commercial use subject to its notice; output rights are not separately established. |
| [Enzo](https://github.com/parkerbritt/enzo) · [website](https://enzo3d.com/) | Node-based procedural modeling with scripting and a headless engine. | MIT code; the maintainer says commercial use is allowed. Early alpha, not production-ready; macOS support is not official. Not an asset pack. |
| [CADAM](https://github.com/Adam-CAD/CADAM) | Web-based text-to-CAD workflow producing editable OpenSCAD programs and STL/DXF exports. | Application GPL-3.0; distribution carries GPL obligations. AI generation requires external model services; output rights are not separately established. |
| [ZENO](https://github.com/zenustech/zeno) | Node-based procedural modeling and simulation with editable example graphs. | Code MPL-2.0, which permits commercial use subject to its file-level conditions; example-asset and output rights need separate confirmation. |
| [TopoTopo](https://github.com/topotopo-dev/topotopo) | Editable JSON node graphs and a procedural geometry engine, with example graphs and exports to 3D tools. | Apache-2.0 code; check third-party notices and asset rights. An engine and examples rather than a finished game-asset pack. |

### Create or customize assets

| Resource | What is available | Requirements and license |
| --- | --- | --- |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [datasets](https://huggingface.co/collections/Sandflow/sand3d) | Parameterized Python parts, joints and assemblies plus five collections of reconstructed object programs. | Library Apache-2.0; dataset cards label programs/renders/USD CC BY 4.0 and retain source licenses and attribution. See [dataset notes](RESOURCES.md#asset-libraries-and-production-tools), including CADFS and AutoMate source-rights caveats. |
| [Infinigen](https://github.com/princeton-vl/infinigen) | Blender/Python procedural generators for natural and indoor scenes and individual objects, with export workflows. | Source repository BSD-3-Clause; output and third-party content rights are not established by that code license. Requires a compatible Blender environment and compute; not a ready-made model pack. |
| [Game assets by holokat](https://github.com/holokat/game-assets) · [playground](https://assets.brackenwake.com/) | Three.js procedural characters, equipment, effects and models, plus downloadable GLBs and Blender-source collections. | Project-authored code and assets MIT; retargeted Quaternius motions are CC0 according to the project. Check the repository's individual third-party notices. |
| [SeedThree](https://github.com/SkyeShark/SeedThree) · [live demo](https://skyeshark.github.io/SeedThree/) | Tune procedural trees and plants for Three.js and export GLB. | MIT repository; early alpha. The project targets WebGPU and describes a WebGL2 fallback. Check individual asset rights and actual device behavior. |
| [FI ShipKit](https://github.com/savannah-i-g/fi-shipkit) | Blender Geometry Nodes kits and Python build scripts for procedural spaceships, stations and structures. | Blender 4.5+ per maintainer; code GPL-3.0-or-later, authored kit files and documentation CC BY 4.0. Check the project's separate terms and dependencies for the intended use. |
| [DragonGraph Geometry Nodes Toolset](https://github.com/Breathfang/BreathfangGeoNodes) | Reusable Blender Geometry Nodes and shader-node assets for procedural modeling. | GPL-3.0 repository; version requirements differ by pack. The maintainer recommends official releases and warns that hosted documentation may lag. |
| [ThreeJS Generator](https://github.com/wearywas/threejs-generator) | Editable Three.js asset programs with procedural controls, three starters and JS/GLB export. | Repository MIT; generated-output rights are not stated separately. AI generation requires model access; not independently run. |
| [Procedura](https://github.com/SpatiaOS/Procedura) | An agent workflow producing editable, part-based OpenSCAD programs and model exports. | Repository MIT; output rights are not separately established. Requires an agent and local dependencies including OpenSCAD and Blender; not a prebuilt model pack. |
| [Polyfork](https://polyfork.dev/) · [license](https://polyfork.dev/licensing) | Low-poly models with adjustable Three.js ES modules and mesh exports; the GitHub catalog is an index, not the model source. | Free model meshes offer CC BY 4.0 or a custom license. ES-module source uses the custom license, which permits project use and modification but restricts standalone redistribution and use in commercial asset generators; it is not open-source code. Account may be required for downloads. |
| [Imaginu](https://github.com/vicotrbb/imaginu) | Rust tool and editable JSON recipes for procedural 3D objects, characters and scenes, exported as GLB. | Repository MIT; output and gallery asset rights are not separately established. Requires Rust for source builds; not independently run. |
| [Dungeon Forge](https://github.com/majidmanzarpour/threejs-procedural-dungeon) | Editable Three.js code generates themed dungeon scenes and procedural geometry from adjustable seeds. | Repository MIT; a scene generator rather than a general model library. Not independently run. |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | Editable OpenSCAD modules for gears, bearings, motors and other parametric mechanical parts. | Primarily LGPL 2.1; individual files may allow more permissive terms. Engineering/CAD-oriented; game use may require mesh conversion and materials. |

### Visual node and parameter libraries

These tools expose editable nodes or parameters; their application source code is not established as public. Pricing and terms can change.

| Resource | What is available | Requirements and license |
| --- | --- | --- |
| [TesselBee](https://tesselbee.com/en) | Browser node graphs and expressions for procedural geometry and textures; publishes adjustable graphs and exports glTF/USD. | WebGPU browser required. Reuse terms for public graphs and exported assets were not confirmed; do not assume the application is open source. |
| [Metropolygonia](https://metropolygonia.com/) · [asset license](https://metropolygonia.com/legal/asset-license/) | Adjustable procedural buildings and cities, with model exports. | Free Beta exports require login and are non-commercial; public projects require attribution and raw-asset redistribution is prohibited. Check the license attached to the particular export. |
| [OmniKit3D](https://www.omnikit3d.com/) · [plans and terms](https://www.omnikit3d.com/pricing) | Blender Geometry Nodes, shaders and scene setups; paid plans provide editable Blender source files. | Catalog previews are free but the source ZIP is paid. Paid plans state a commercial license for a named creator or seat; check the seller's exact terms and third-party rights. |

### Research and evaluation datasets

| Resource | What is available | Requirements and license |
| --- | --- | --- |
| [CadQuarry](https://huggingface.co/datasets/jacobjennings/cadquarry) · [generator](https://github.com/jacobjennings/CadQuarry) | Parameterized CadQuery programs and mechanical CAD models, including STEP/STL. | Dataset card states data CC0-1.0 and generator Apache-2.0; check dependencies. Engineering research data, not a game-ready pack; not independently run. |
| [NovaSceneSmith](https://huggingface.co/datasets/raresense/nova-scenesmith) | 20 generated indoor simulation scenes with editable Python source, GLB and simulation exports. | Dataset card marks Apache-2.0; its credits distinguish the original descriptions and other upstream material. Research scenes, not a curated game pack; files were not independently run. |
| [SpaceCode-Bench](https://huggingface.co/datasets/KurtDu/SpaceCode-Bench) | Research benchmark with native Blender environments, construction, reconstruction and editing tasks. | Dataset card labels CC BY 4.0. Native scenes are evaluation data, not a curated game-asset pack; source rights and dependencies should be checked separately. |
| [FoldNet](https://huggingface.co/datasets/Bowie375/FoldNet) · [generator code](https://github.com/chen01yx/FoldNet_code) | Research dataset of procedurally generated clothing assets and associated reconstruction code. | Dataset card labels CC BY 4.0; a separate generator-code license was not found. The full dataset viewer reported a generation error when checked; files and generator were not independently tested. |
| [3DCodeBench](https://huggingface.co/datasets/3dcodebench/3dcodebench) · [expanded corpus](https://huggingface.co/datasets/YipengGao/3DCodeBench) | 212 benchmark tasks with Blender Python scripts, prompts, reference renders and exported GLB meshes. | Dataset card marks procedural code, meshes, reference renders and captions BSD-3-Clause. Benchmark data rather than a curated game-ready pack; the card says its upload is anonymous pending review. The dataset viewer was unavailable when checked. The expanded corpus reports 12,720 instances; its Infinigen-derived scripts retain BSD-3-Clause while its card labels other materials MIT. |
| [3DCodeVerse-2M](https://huggingface.co/datasets/3dcodeverse/3dcodeverse-2m) · [project](https://3dcodeverse.com/) | A research corpus spanning Blender Python, CadQuery, Three.js, GLSL, OpenSCAD and URDF, with renders and some meshes. | Dataset card labels the collection CC BY-NC-SA 4.0 for non-commercial research; source licenses vary and stricter terms apply. It is not a blanket commercial game-asset license. The dataset viewer was unavailable when checked. |

The publisher describes about 2.03 million code–condition pairs drawn from 269,597 executable programs for 3DCodeVerse; pairs are not necessarily distinct models. This catalog lists original locations and does not redistribute the material.

## 简体中文

这里收录可编辑代码、程序化生成器和 3D 对象研究数据集。这些都是**通用 3D 资源**，不代表项目使用了 Fable 5.2。来源核查于 2026 年 11 月 12 日（UTC+8），详见[检索记录](CODE-ASSET-SEARCH-LOG.md)；本项目未独立运行或渲染这些资源。代码库、数据集、第三方素材与生成结果的许可应分别核对。

### 可商用的开源代码与节点资产

下列项目代码或素材的许可允许按各自条款商用；涉及第三方素材和生成结果时，仍需分别查看。项目尚未由我们独立运行。

| 资源 | 可编辑内容 | 许可与使用说明 |
| --- | --- | --- |
| [ModKit](https://github.com/JaronKBragg7337/asset-pack-ue-threejs-blender-unity) | 程序化生成的模块化建筑与道具，提供 Blender 源文件、脚本和 GLB/FBX 导出。 | 项目将网格、脚本和渲染图标为 CC0-1.0；第三方内容仍须单独核对。 |
| [NeuralStock](https://github.com/Neuralstock/neuralstock) | Room Zero 室内组合资产，含 Blender 源文件、程序化生成器和 GLB 素材。 | 仓库软件为 MIT；资产政策将已发布素材标为 CC0-1.0。来源和验证情况由维护者报告，使用时核对各版本的权利记录。 |
| [CGFigures Asset Library](https://www.cgfigures.ca/assetlibrary) | 面向科学可视化的 Blender 资产浏览器素材库，含可编辑模型和节点工具。 | 创建者标为 CC0 1.0；免费和付费版本据称内容相同。尚未独立检查下载文件。 |
| [RFX Blender Asset Library](https://github.com/Pixelguru26/RFX-Blender-Asset-Library) | Blender 几何节点、修改器、材质和纹理，包括硬表面与科幻建模工具。 | CC0-1.0；维护者允许使用、修改和再分发。部分资产仍在制作中。 |
| [Primitive Assets Library](https://github.com/pesaksintondji/primitive-assets-library) | Blender 几何节点基础形状和硬表面零件，附重建素材库的 Python 脚本。 | 素材和脚本为 CC0-1.0；需要兼容的 Blender 版本。 |
| [Geometry Node Asset Files](https://github.com/johnnygizmo/node_assets) | 可用于 Blender 资产浏览器的 `.blend` 节点组。 | CC0-1.0；维护者说明文件使用 Blender 每日构建版制作，需检查版本兼容性。 |
| [Procedural 3D assets](https://github.com/boytchev/3d-assets) | 一组可逐项编辑的 Three.js 程序化物件源码。 | 仓库为 MIT；再分发代码时保留版权及许可声明。单独的素材与输出权利需核对。 |
| [Cosmo Tree Gen](https://github.com/FrogCosmonaut/cosmo_tree_gen) | Godot 树木生成器，可调整参数与预设，支持 LOD 和 GLB/glTF 导出。 | 代码为 MIT；需要 Godot 4.6+。项目注明叶片纹理为 CC0、树皮纹理来自 ambientCG；使用时查看附带的第三方说明。 |
| [SimpleXTerrain](https://github.com/prajwal-mx/SimpleXTerrain) | Godot 节点式地形生成器，可编辑生物群系、噪声和侵蚀规则。 | 代码为 MIT；需要 Godot .NET 和 Terrain3D。它在引擎内生成地形，不是独立模型素材包。 |
| [Godot Road Generator](https://github.com/TheDuckCow/godot-road-generator) | 参数化道路、路口和车道，提供可编辑的 Godot 源码及 glTF 导出。 | 代码为 MIT；需要 Godot 4.4+。内置素材应查看项目与第三方许可说明。 |
| [TreeForge](https://github.com/Kapilthakur1520/treeforge) | 用于可视化与 3D 资产的参数化树木生成器。 | 代码为 MIT，可按条款商用并保留许可声明；生成结果权利未单独确认。 |
| [Enzo](https://github.com/parkerbritt/enzo) · [官网](https://enzo3d.com/) | 支持脚本和无界面运行的节点式程序化建模引擎。 | 代码为 MIT；维护者说明可商用。处于早期 alpha，不建议直接用于生产流程；macOS 尚无官方支持。这是工具而非现成素材包。 |
| [CADAM](https://github.com/Adam-CAD/CADAM) | 网页文字转 CAD 工具，可生成可编辑的 OpenSCAD 程序并导出 STL/DXF。 | 应用为 GPL-3.0；分发时须履行 GPL 义务。AI 生成功能需要外部模型服务；生成结果权利未单独确认。 |
| [ZENO](https://github.com/zenustech/zeno) | 节点式程序化建模与仿真工具，附可编辑示例节点图。 | 代码为 MPL-2.0，允许按其文件级条件商用；示例素材与生成结果的权利须单独确认。 |
| [TopoTopo](https://github.com/topotopo-dev/topotopo) | 可编辑 JSON 节点图与程序化几何引擎，附示例图并支持导出到 3D 工具。 | 代码为 Apache-2.0；需查看第三方声明与素材权利。这是引擎和示例，而非成品游戏素材包。 |

### 创建和定制资产

| 资源 | 可获得什么 | 依赖与许可 |
| --- | --- | --- |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [数据集](https://huggingface.co/collections/Sandflow/sand3d) | 参数化 Python 零件、关节和装配体，以及五组重建对象的程序。 | 建模库为 Apache-2.0；数据卡将程序、渲染图和 USD 标为 CC BY 4.0，保留来源许可与署名。CADFS 和 AutoMate 的原始权利提示等详见[数据集说明](RESOURCES.md#资产库与制作工具)。 |
| [Infinigen](https://github.com/princeton-vl/infinigen) | 使用 Blender/Python 程序化生成自然场景、室内场景和单个对象，并提供导出流程。 | 源码仓库为 BSD-3-Clause；代码许可不能直接说明生成结果和第三方内容的权利。需要兼容的 Blender 环境与算力，并非现成模型包。 |
| [holokat 游戏资产](https://github.com/holokat/game-assets) · [试玩与浏览](https://assets.brackenwake.com/) | Three.js 程序化角色、装备、特效和模型，另有可下载 GLB 与 Blender 源文件素材。 | 项目自制代码和资产为 MIT；按项目说明，重定向的 Quaternius 动作为 CC0。仍应查看仓库内各第三方许可说明。 |
| [SeedThree](https://github.com/SkyeShark/SeedThree) · [在线演示](https://skyeshark.github.io/SeedThree/) | 调整 Three.js 程序化树木与植物参数，导出 GLB。 | 仓库为 MIT；处于早期 alpha。项目以 WebGPU 为主要路径，并说明有 WebGL2 降级；需核对具体素材权利及设备效果。 |
| [FI ShipKit](https://github.com/savannah-i-g/fi-shipkit) | 使用 Blender 几何节点素材和 Python 构建脚本，程序化制作飞船、空间站及建筑。 | 维护者说明需要 Blender 4.5+；代码为 GPL-3.0-or-later，自制 kit 文件和文档为 CC BY 4.0。使用前分别查看项目条款及依赖。 |
| [DragonGraph 几何节点工具集](https://github.com/Breathfang/BreathfangGeoNodes) | 用于程序化建模的 Blender 几何节点与着色器节点资产。 | 仓库为 GPL-3.0；不同素材包的 Blender 版本要求可能不同。维护者建议使用正式发布版本，并提示托管文档可能滞后。 |
| [ThreeJS Generator](https://github.com/wearywas/threejs-generator) | 可编辑的 Three.js 资产程序，支持程序化参数、三个起始示例及 JS/GLB 导出。 | 仓库为 MIT；未找到单独的生成结果许可。AI 生成功能需要模型访问；尚未独立运行。 |
| [Procedura](https://github.com/SpatiaOS/Procedura) | 由智能体制作可编辑、按零件组织的 OpenSCAD 程序并导出模型。 | 仓库为 MIT；生成结果权利未单独确认。需要智能体及 OpenSCAD、Blender 等本地依赖；不是现成模型包。 |
| [Polyfork](https://polyfork.dev/) · [许可](https://polyfork.dev/licensing) | 低多边形模型及可调整的 Three.js ES 模块，可导出网格；GitHub 仓库是索引，并不托管模型源码。 | 免费模型网格可选 CC BY 4.0 或自定义许可；ES 模块源码适用自定义许可，允许项目内使用和修改，但限制独立再分发及用于商业资产生成器，不能称为开源代码。下载可能需要账号。 |
| [Imaginu](https://github.com/vicotrbb/imaginu) | 使用 Rust 工具和可编辑 JSON 配方生成 3D 物件、角色及场景并导出 GLB。 | 仓库为 MIT；生成结果及展示素材的权利未单独确认。源码构建需要 Rust；尚未独立运行。 |
| [Dungeon Forge](https://github.com/majidmanzarpour/threejs-procedural-dungeon) | 可编辑的 Three.js 代码通过可调随机种子生成不同主题的地牢场景及程序化几何体。 | 仓库为 MIT；这是场景生成器，并非通用模型库。尚未独立运行。 |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | 可编辑的 OpenSCAD 参数化齿轮、轴承、电机等机械零件模块。 | 主要采用 LGPL 2.1，个别文件可能提供更宽松条款。偏工程 CAD，用于游戏时可能需要转换网格和制作材质。 |

### 可编辑节点和参数素材库

这些工具提供可调整的节点或参数；尚未确认其应用程序源码公开。价格与条款可能变化。

| 资源 | 可获得什么 | 依赖与许可 |
| --- | --- | --- |
| [TesselBee](https://tesselbee.com/en) | 浏览器中的程序化几何与纹理节点图和表达式，可发布可调节的节点图并导出 glTF/USD。 | 需要支持 WebGPU 的浏览器。公开节点图及导出资产的再利用条款未确认；不能据此认定应用开源。 |
| [Metropolygonia](https://metropolygonia.com/) · [资产许可](https://metropolygonia.com/legal/asset-license/) | 可调整的程序化建筑和城市，支持模型导出。 | 免费 Beta 导出需要登录且仅限非商业用途；公开作品须署名，禁止单独再分发原始资产。以具体导出时附带的许可为准。 |
| [OmniKit3D](https://www.omnikit3d.com/) · [方案与条款](https://www.omnikit3d.com/pricing) | Blender 几何节点、着色器与场景素材；付费方案提供可编辑的 Blender 源文件。 | 素材目录可免费预览，源码 ZIP 需付费。付费方案说明包含针对指定创作者或席位的商业许可；购买前核对卖家具体条款和第三方权利。 |

### 研究与评测数据集

| 资源 | 可获得什么 | 依赖与许可 |
| --- | --- | --- |
| [CadQuarry](https://huggingface.co/datasets/jacobjennings/cadquarry) · [生成器](https://github.com/jacobjennings/CadQuarry) | 参数化 CadQuery 程序和机械 CAD 模型，包括 STEP/STL。 | 数据卡注明数据为 CC0-1.0、生成器为 Apache-2.0；需核对依赖。这是工程研究数据，并非现成游戏素材包；尚未独立运行。 |
| [NovaSceneSmith](https://huggingface.co/datasets/raresense/nova-scenesmith) | 20 个生成式室内仿真场景，附可编辑 Python 源码、GLB 和仿真格式导出。 | 数据卡标为 Apache-2.0；来源说明区分原始场景描述及其他上游材料。这是研究场景，并非专门整理的游戏素材包；尚未独立运行文件。 |
| [SpaceCode-Bench](https://huggingface.co/datasets/KurtDu/SpaceCode-Bench) | 含 Blender 原生场景的研究评测集，覆盖场景构建、重建和编辑任务。 | 数据卡标为 CC BY 4.0。原生场景属于评测数据，并非专门整理的游戏素材包；应分别核对来源权利和依赖。 |
| [FoldNet](https://huggingface.co/datasets/Bowie375/FoldNet) · [生成代码](https://github.com/chen01yx/FoldNet_code) | 程序化生成的服装资产研究数据及相关重建代码。 | 数据卡标为 CC BY 4.0；未找到生成代码的独立许可证。检查时完整数据集浏览器报告生成错误；文件和生成器尚未独立测试。 |
| [3DCodeBench](https://huggingface.co/datasets/3dcodebench/3dcodebench) · [扩展语料](https://huggingface.co/datasets/YipengGao/3DCodeBench) | 212 个评测任务，包含 Blender Python 脚本、提示词、参考渲染图与导出的 GLB 网格。 | 数据卡将程序代码、网格、参考渲染图和文本标为 BSD-3-Clause。这是评测数据，不是专门筛选的游戏素材包；数据卡说明投稿评审期间匿名，检查时数据集浏览器不可用。扩展语料报告有 12,720 个实例；其源自 Infinigen 的脚本保留 BSD-3-Clause，数据卡将其他材料标为 MIT。 |
| [3DCodeVerse-2M](https://huggingface.co/datasets/3dcodeverse/3dcodeverse-2m) · [项目主页](https://3dcodeverse.com/) | 覆盖 Blender Python、CadQuery、Three.js、GLSL、OpenSCAD 和 URDF 的研究代码数据，附渲染图和部分网格。 | 数据卡将整体标为 CC BY-NC-SA 4.0，仅供非商业研究；不同来源许可不同，适用更严格的条款。不能据此认为整库可用于商业游戏；检查时数据集浏览器不可用。 |

3DCodeVerse 发布方称，约 203 万条代码与条件配对来自 269,597 个可执行程序；配对数不等于独立模型数。本目录只链接原始位置，不复制素材。

# 3D assets as code / 代码构建的 3D 资产

[English](#english) | [简体中文](#简体中文)

## English

A selection of editable code, procedural generators and research datasets for 3D objects. These are **general 3D resources**, not claims of Fable 5.2 use. Sources were checked on 12 November 2026 (UTC+8); see the [search log](CODE-ASSET-SEARCH-LOG.md). Projects and assets were not independently run or rendered. Check the license of each codebase, dataset, third-party asset and output separately.

### Create or customize assets

| Resource | What is available | Requirements and license |
| --- | --- | --- |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [datasets](https://huggingface.co/collections/Sandflow/sand3d) | Parameterized Python parts, joints and assemblies plus five collections of reconstructed object programs. | Library Apache-2.0; dataset cards label programs/renders/USD CC BY 4.0 and retain source licenses and attribution. See [dataset notes](RESOURCES.md#asset-libraries-and-production-tools), including CADFS and AutoMate source-rights caveats. |
| [Infinigen](https://github.com/princeton-vl/infinigen) | Blender/Python procedural generators for natural and indoor scenes and individual objects, with export workflows. | Source repository BSD-3-Clause; output and third-party content rights are not established by that code license. Requires a compatible Blender environment and compute; not a ready-made model pack. |
| [Game assets by holokat](https://github.com/holokat/game-assets) · [playground](https://assets.brackenwake.com/) | Three.js procedural characters, equipment, effects and models, plus downloadable GLBs and Blender-source collections. | Project-authored code and assets MIT; retargeted Quaternius motions are CC0 according to the project. Check the repository's individual third-party notices. |
| [SeedThree](https://github.com/SkyeShark/SeedThree) · [live demo](https://skyeshark.github.io/SeedThree/) | Tune procedural trees and plants for Three.js and export GLB. | MIT repository; early alpha. The project targets WebGPU and describes a WebGL2 fallback. Check individual asset rights and actual device behavior. |
| [FI ShipKit](https://github.com/savannah-i-g/fi-shipkit) | Blender Geometry Nodes kits and Python build scripts for procedural spaceships, stations and structures. | Blender 4.5+ per maintainer; code GPL-3.0-or-later, authored kit files and documentation CC BY 4.0. Check the project's separate terms and dependencies for the intended use. |
| [DragonGraph Geometry Nodes Toolset](https://github.com/Breathfang/BreathfangGeoNodes) | Reusable Blender Geometry Nodes and shader-node assets for procedural modeling. | GPL-3.0 repository; version requirements differ by pack. The maintainer recommends official releases and warns that hosted documentation may lag. |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | Editable OpenSCAD modules for gears, bearings, motors and other parametric mechanical parts. | Primarily LGPL 2.1; individual files may allow more permissive terms. Engineering/CAD-oriented; game use may require mesh conversion and materials. |

### Research and evaluation datasets

| Resource | What is available | Requirements and license |
| --- | --- | --- |
| [FoldNet](https://huggingface.co/datasets/Bowie375/FoldNet) · [generator code](https://github.com/chen01yx/FoldNet_code) | Research dataset of procedurally generated clothing assets and associated reconstruction code. | Dataset card labels CC BY 4.0; a separate generator-code license was not found. The full dataset viewer reported a generation error when checked; files and generator were not independently tested. |
| [3DCodeBench](https://huggingface.co/datasets/3dcodebench/3dcodebench) | 212 benchmark tasks with Blender Python scripts, prompts, reference renders and exported GLB meshes. | Dataset card marks procedural code, meshes, reference renders and captions BSD-3-Clause. Benchmark data rather than a curated game-ready pack; the card says its upload is anonymous pending review. The dataset viewer was unavailable when checked. |
| [3DCodeVerse-2M](https://huggingface.co/datasets/3dcodeverse/3dcodeverse-2m) · [project](https://3dcodeverse.com/) | A research corpus spanning Blender Python, CadQuery, Three.js, GLSL, OpenSCAD and URDF, with renders and some meshes. | Dataset card labels the collection CC BY-NC-SA 4.0 for non-commercial research; source licenses vary and stricter terms apply. It is not a blanket commercial game-asset license. The dataset viewer was unavailable when checked. |

The publisher describes about 2.03 million code–condition pairs drawn from 269,597 executable programs for 3DCodeVerse; pairs are not necessarily distinct models. This catalog lists original locations and does not redistribute the material.

## 简体中文

这里收录可编辑代码、程序化生成器和 3D 对象研究数据集。这些都是**通用 3D 资源**，不代表项目使用了 Fable 5.2。来源核查于 2026 年 11 月 12 日（UTC+8），详见[检索记录](CODE-ASSET-SEARCH-LOG.md)；本项目未独立运行或渲染这些资源。代码库、数据集、第三方素材与生成结果的许可应分别核对。

### 创建和定制资产

| 资源 | 可获得什么 | 依赖与许可 |
| --- | --- | --- |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [数据集](https://huggingface.co/collections/Sandflow/sand3d) | 参数化 Python 零件、关节和装配体，以及五组重建对象的程序。 | 建模库为 Apache-2.0；数据卡将程序、渲染图和 USD 标为 CC BY 4.0，保留来源许可与署名。CADFS 和 AutoMate 的原始权利提示等详见[数据集说明](RESOURCES.md#资产库与制作工具)。 |
| [Infinigen](https://github.com/princeton-vl/infinigen) | 使用 Blender/Python 程序化生成自然场景、室内场景和单个对象，并提供导出流程。 | 源码仓库为 BSD-3-Clause；代码许可不能直接说明生成结果和第三方内容的权利。需要兼容的 Blender 环境与算力，并非现成模型包。 |
| [holokat 游戏资产](https://github.com/holokat/game-assets) · [试玩与浏览](https://assets.brackenwake.com/) | Three.js 程序化角色、装备、特效和模型，另有可下载 GLB 与 Blender 源文件素材。 | 项目自制代码和资产为 MIT；按项目说明，重定向的 Quaternius 动作为 CC0。仍应查看仓库内各第三方许可说明。 |
| [SeedThree](https://github.com/SkyeShark/SeedThree) · [在线演示](https://skyeshark.github.io/SeedThree/) | 调整 Three.js 程序化树木与植物参数，导出 GLB。 | 仓库为 MIT；处于早期 alpha。项目以 WebGPU 为主要路径，并说明有 WebGL2 降级；需核对具体素材权利及设备效果。 |
| [FI ShipKit](https://github.com/savannah-i-g/fi-shipkit) | 使用 Blender 几何节点素材和 Python 构建脚本，程序化制作飞船、空间站及建筑。 | 维护者说明需要 Blender 4.5+；代码为 GPL-3.0-or-later，自制 kit 文件和文档为 CC BY 4.0。使用前分别查看项目条款及依赖。 |
| [DragonGraph 几何节点工具集](https://github.com/Breathfang/BreathfangGeoNodes) | 用于程序化建模的 Blender 几何节点与着色器节点资产。 | 仓库为 GPL-3.0；不同素材包的 Blender 版本要求可能不同。维护者建议使用正式发布版本，并提示托管文档可能滞后。 |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | 可编辑的 OpenSCAD 参数化齿轮、轴承、电机等机械零件模块。 | 主要采用 LGPL 2.1，个别文件可能提供更宽松条款。偏工程 CAD，用于游戏时可能需要转换网格和制作材质。 |

### 研究与评测数据集

| 资源 | 可获得什么 | 依赖与许可 |
| --- | --- | --- |
| [FoldNet](https://huggingface.co/datasets/Bowie375/FoldNet) · [生成代码](https://github.com/chen01yx/FoldNet_code) | 程序化生成的服装资产研究数据及相关重建代码。 | 数据卡标为 CC BY 4.0；未找到生成代码的独立许可证。检查时完整数据集浏览器报告生成错误；文件和生成器尚未独立测试。 |
| [3DCodeBench](https://huggingface.co/datasets/3dcodebench/3dcodebench) | 212 个评测任务，包含 Blender Python 脚本、提示词、参考渲染图与导出的 GLB 网格。 | 数据卡将程序代码、网格、参考渲染图和文本标为 BSD-3-Clause。这是评测数据，不是专门筛选的游戏素材包；数据卡说明投稿评审期间匿名，检查时数据集浏览器不可用。 |
| [3DCodeVerse-2M](https://huggingface.co/datasets/3dcodeverse/3dcodeverse-2m) · [项目主页](https://3dcodeverse.com/) | 覆盖 Blender Python、CadQuery、Three.js、GLSL、OpenSCAD 和 URDF 的研究代码数据，附渲染图和部分网格。 | 数据卡将整体标为 CC BY-NC-SA 4.0，仅供非商业研究；不同来源许可不同，适用更严格的条款。不能据此认为整库可用于商业游戏；检查时数据集浏览器不可用。 |

3DCodeVerse 发布方称，约 203 万条代码与条件配对来自 269,597 个可执行程序；配对数不等于独立模型数。本目录只链接原始位置，不复制素材。

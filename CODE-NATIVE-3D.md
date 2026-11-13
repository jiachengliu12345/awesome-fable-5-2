# Code-native 3D assets / 代码原生 3D 资产

[English](#english) | [简体中文](#简体中文)

## English

These resources provide **editable source code that generates or defines 3D objects, scenes, materials or effects**. They are general resources for a Fable 5.2 workflow; inclusion does not establish that Fable created them. A model file without its generating code, an image-only demo, and a visual node graph without editable source are outside this selection. Code licenses and the rights to bundled assets or generated output are separate; verify both for your intended use. Projects were not independently run.

For the broader collection, including node graphs and datasets, see [3D assets as code](CODE-ASSETS.md#english).

<details>
<summary>Objects, architecture and reusable parts</summary>

| Resource and source | What the code generates | License and constraints |
| --- | --- | --- |
| [Procedural 3D assets](https://github.com/boytchev/3d-assets) | Individually editable Three.js object programs. | MIT code; check separate content and outputs. |
| [Game assets by holokat](https://github.com/holokat/game-assets) | Three.js characters, equipment, effects and models; includes other asset formats. | Project-authored code and assets MIT; check third-party notices, including CC0 motions. |
| [Arch Generator](https://github.com/Aniruddhyagoswami/arch_generator) | Blender Python for parameterized arches, pillars and architectural arrays. | GPL-3.0-or-later; distribution of modified code has GPL obligations. Check other included assets and output rights. |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | Parameterized OpenSCAD gears, bearings, motors and other mechanical parts. | Primarily LGPL-2.1; inspect individual file licenses. CAD parts may need conversion for games. |
| [SeedThree](https://github.com/SkyeShark/SeedThree) | Three.js procedural trees and plants with parameters and GLB export. | MIT code; early alpha, individual asset rights require checking. |
| [Lowpoly Tree Generator](https://github.com/pajama-studio/lowpoly-tree-generator) | Parameterized Three.js low-poly trees with animation and GLB export. | MIT code; retain third-party notices and check assets separately. |
| [EZ-Tree](https://github.com/dgreenheck/ez-tree) | Configurable Three.js trees with GLB/PNG export. | MIT repository; check included textures and any third-party notices. |

</details>

<details>
<summary>Worlds, terrain and scene generation</summary>

| Resource and source | What the code generates | License and constraints |
| --- | --- | --- |
| [Dungeon Forge](https://github.com/majidmanzarpour/threejs-procedural-dungeon) | Seeded Three.js dungeon scenes and geometry. | MIT repository; check third-party and output rights separately. |
| [Infinigen](https://github.com/princeton-vl/infinigen) | Blender/Python generators for natural and indoor scenes and objects. | BSD-3-Clause code; output and third-party rights require separate checks. |
| [Cartoon Terrain Studio](https://github.com/idlerunner00/cartoon-terrain-studio) | Godot C# and shaders for editable stylized 2.5D terrain; the maintainer describes its visuals as code-generated. | MIT repository; check dependencies and output rights. Requires Godot .NET. |
| [Architectural Design Pipeline](https://github.com/Mhrnqaruni/architectural-design-pipeline) | Python parametric house design generates CAD and a furnished Three.js model. | MIT project code; PDF/PNG pipeline uses PyMuPDF, with separate AGPL/commercial terms. Check all dependency and output rights. |

</details>

<details>
<summary>Materials and effects</summary>

| Resource and source | What the code generates | License and constraints |
| --- | --- | --- |
| [WebGL Shader Lab](https://github.com/PSCactux/webgl-shader-lab) | Editable Three.js / React Three Fiber shader, particle, terrain and geometry examples. | MIT repository; Node 20+ and WebGL2; verify third-party and output rights. |

</details>

<details>
<summary>Code-building foundations</summary>

| Resource and source | What the code provides | License and constraints |
| --- | --- | --- |
| [ProcFunc](https://github.com/princeton-vl/procfunc) | Python procedural primitives and conversion from Blender Geometry Nodes to editable code. | BSD-3-Clause; API before 1.0, with separately licensed generators and assets. |
| [CCORE Three.js 3D GLB Assets](https://huggingface.co/datasets/ccore/ThreeJS-3D-GLB-Assets) | Research examples with editable HTML/Three.js in the `conversations` dataset configuration and corresponding GLBs. | Dataset card declares MIT only to the extent of publisher rights; item-level provenance is unverified. Publisher-reported validation, not independently reproduced. |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [datasets](https://huggingface.co/collections/Sandflow/sand3d) | Parameterized Python objects, joints and assemblies, plus reconstructed-object programs. | Library Apache-2.0; dataset records carry their own attribution and source-license caveats. See [dataset notes](resources/ASSET-TOOLS.md#asset-libraries-and-production-tools). |

</details>

## 简体中文

这里收集**以可编辑源码生成或定义 3D 物件、场景、材质或特效**的资源，可供 Fable 5.2 工作流参考；收录不代表这些项目由 Fable 制作。只有模型文件而没有生成代码、只有图片演示、或只有可视化节点图而没有可编辑源码的项目，不放入本精选。代码、附带素材和生成结果的权利应分别核对；本次没有独立运行这些项目。

更广泛的节点素材与数据集见 [代码构建的 3D 资产](CODE-ASSETS.md#简体中文)。

<details>
<summary>物件、建筑与可复用零件</summary>

| 资源与源码 | 代码生成什么 | 许可与限制 |
| --- | --- | --- |
| [Procedural 3D assets](https://github.com/boytchev/3d-assets) | 可逐个修改的 Three.js 物件生成代码。 | 代码 MIT；单独素材和输出需核对。 |
| [Game assets by holokat](https://github.com/holokat/game-assets) | Three.js 角色、装备、特效和模型，也包含其他资产格式。 | 项目自制代码与资产为 MIT；需核对第三方声明，包括 CC0 动作。 |
| [Arch Generator](https://github.com/Aniruddhyagoswami/arch_generator) | 使用 Blender Python 参数化生成拱门、柱子和建筑构件阵列。 | GPL-3.0-or-later；分发修改后的代码须遵守 GPL。其他附带素材和输出权利需核对。 |
| [OpenSCAD MCAD](https://github.com/openscad/MCAD) | 参数化 OpenSCAD 齿轮、轴承、电机等机械零件。 | 主要为 LGPL-2.1；应核对各文件许可。用于游戏时可能需要转换格式。 |
| [SeedThree](https://github.com/SkyeShark/SeedThree) | 可调整参数的 Three.js 树木和植物，支持 GLB 导出。 | 代码 MIT；处于早期 alpha，具体素材权利需核对。 |
| [Lowpoly Tree Generator](https://github.com/pajama-studio/lowpoly-tree-generator) | 参数化 Three.js 低多边形树木，支持动画和 GLB 导出。 | 代码 MIT；保留第三方声明，素材需分别核对。 |
| [EZ-Tree](https://github.com/dgreenheck/ez-tree) | 可配置的 Three.js 树木，支持 GLB/PNG 导出。 | 仓库 MIT；需核对附带纹理及第三方声明。 |

</details>

<details>
<summary>世界、地形与场景生成</summary>

| 资源与源码 | 代码生成什么 | 许可与限制 |
| --- | --- | --- |
| [Dungeon Forge](https://github.com/majidmanzarpour/threejs-procedural-dungeon) | 根据种子生成 Three.js 地牢场景和几何体。 | 仓库 MIT；第三方素材及输出权利需分别核对。 |
| [Infinigen](https://github.com/princeton-vl/infinigen) | Blender/Python 自然与室内场景及物体生成器。 | 代码 BSD-3-Clause；输出和第三方素材的权利需单独核对。 |
| [Cartoon Terrain Studio](https://github.com/idlerunner00/cartoon-terrain-studio) | 用 Godot C# 和着色器生成可编辑的风格化 2.5D 地形；维护者说明画面由代码生成。 | 仓库 MIT；需核对依赖和输出权利，使用 Godot .NET。 |
| [Architectural Design Pipeline](https://github.com/Mhrnqaruni/architectural-design-pipeline) | Python 参数化住宅设计生成 CAD 图纸和带家具的 Three.js 模型。 | 项目代码 MIT；PDF/PNG 流程使用 PyMuPDF，适用其单独的 AGPL 或商业条款。依赖和输出权利需核对。 |

</details>

<details>
<summary>材质与特效</summary>

| 资源与源码 | 代码生成什么 | 许可与限制 |
| --- | --- | --- |
| [WebGL Shader Lab](https://github.com/PSCactux/webgl-shader-lab) | 可编辑的 Three.js / React Three Fiber 着色器、粒子、地形和几何体示例。 | 仓库 MIT；需要 Node 20+ 和 WebGL2，第三方素材及输出权利需核对。 |

</details>

<details>
<summary>代码构建基础</summary>

| 资源与源码 | 代码提供什么 | 许可与限制 |
| --- | --- | --- |
| [ProcFunc](https://github.com/princeton-vl/procfunc) | Python 程序化基础组件，并支持将 Blender 几何节点转换成可编辑代码。 | BSD-3-Clause；API 尚未到 1.0，其他生成器与素材有各自许可。 |
| [CCORE Three.js 3D GLB Assets](https://huggingface.co/datasets/ccore/ThreeJS-3D-GLB-Assets) | 研究数据集；`conversations` 配置中有可编辑 HTML/Three.js 代码及对应 GLB。 | 数据卡标为 MIT，但仅限发布者持有的权利；逐项来源未核实。验证结果由发布方报告，尚未独立复现。 |
| [Sand3D](https://github.com/Sandflow-ai/sand3d) · [数据集](https://huggingface.co/collections/Sandflow/sand3d) | 参数化 Python 物体、关节和装配体，以及重建对象的程序。 | 建模库 Apache-2.0；数据集记录有各自的来源许可和署名注意事项，详见[数据集说明](resources/ASSET-TOOLS.md#资产库与制作工具)。 |

</details>

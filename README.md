# pytorch-basics-journey

[![CI](https://github.com/edidada/pytorch-basics-journey/actions/workflows/ci.yml/badge.svg)](https://github.com/edidada/pytorch-basics-journey/actions/workflows/ci.yml)

跟随 PyTorch 官方 [Learn the Basics](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) 的练习仓库。目录按知识模块而不是按天/周组织，每个模块可独立运行、可验证。

官方模块顺序：Tensors → Datasets & DataLoaders → Transforms → Build Model → Autograd → Optimization → Save & Load Model，`00_quickstart` 作为总览放在最前，先跑通完整流程再逐个深入。

## 学习进度

| 模块 | 状态 | 完成日期 | 关键收获 |
|---|---|---|---|
| 00 Quickstart | 🚧 | | 骨架已搭好，CI 冒烟测试可跑通完整训练循环 |
| 01 Tensors | ⬜ | | |
| 02 Datasets & DataLoaders | ⬜ | | |
| 03 Transforms | ⬜ | | |
| 04 Build Model | ⬜ | | |
| 05 Autograd | ⬜ | | |
| 06 Optimization | ⬜ | | |
| 07 Save & Load Model | ⬜ | | |

⬜ 未开始 · 🚧 进行中 · ✅ 已完成

## 本地运行

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

各模块下的 `.ipynb` 请从对应官方教程页面下载，运行后保留输出；模块内 `README.md` 只记录三样东西：官方链接、一句话说明、跑通后的关键输出或结论。

## CI

`.github/workflows/ci.yml` 在每次 push / PR 时：

1. 安装 CPU 版 PyTorch（避开 CUDA 依赖下载，加快 CI）；
2. 打印环境信息，并用 `compileall` 编译校验所有 `.py`；
3. 校验所有 `.ipynb` 是合法的 nbformat 4 JSON；
4. 运行 `00_quickstart/quickstart.py` —— 用合成数据跑通「数据 → 模型 → 训练 → 保存/加载 → 推理」，不依赖联网下载数据集。

查看日志：

```bash
gh run list
gh run view <run-id> --log
```

## 目录结构

```text
pytorch-basics-journey/
├── README.md
├── README.txt                  # 最初的仓库规划笔记
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
├── 00_quickstart/ … 07_save_load_model/
│   ├── README.md
│   └── *.ipynb
└── assets/                     # notebook 引用的图片 / 输出截图
```

> `data/`、`*.pth` 等已在 `.gitignore` 中忽略，数据集与模型权重不入库。

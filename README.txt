基于 PyTorch 官方“Learn the Basics”的体系来组织仓库，关键是**让目录结构直接映射官方教程的学习路径**，同时保持每个知识点可独立运行、可验证。下面是一个兼顾学习记录与代码实践的仓库方案。

### 仓库命名建议

推荐使用 `pytorch-basics-journey` 或 `pytorch-official-basics`。名字里带上 “basics” 或 “journey”，既能表明这是跟随官方基础教程的练习仓库，也方便日后回顾时定位内容范围。

### 目录结构

```text
pytorch-basics-journey/
├── README.md
├── requirements.txt
├── .gitignore
├── 00_quickstart/
│   ├── README.md
│   └── quickstart.ipynb
├── 01_tensors/
│   ├── README.md
│   └── tensors.ipynb
├── 02_datasets_dataloaders/
│   ├── README.md
│   └── datasets_dataloaders.ipynb
├── 03_transforms/
│   ├── README.md
│   └── transforms.ipynb
├── 04_build_model/
│   ├── README.md
│   └── build_model.ipynb
├── 05_autograd/
│   ├── README.md
│   └── autograd.ipynb
├── 06_optimization/
│   ├── README.md
│   └── optimization.ipynb
├── 07_save_load_model/
│   ├── README.md
│   └── save_load_model.ipynb
└── assets/
    └── (存放 notebook 里引用的图片或输出截图)
```

### 每个子文件夹的组织逻辑

官方 Quickstart 页面列出的基础模块顺序是：Tensors → Datasets & DataLoaders → Transforms → Build Model → Autograd → Optimization → Save & Load Model。上面的编号 `00` 到 `07` 就是按这个顺序来的，`00_quickstart` 作为总览放在最前面，让你先跑通一个完整流程，再逐个模块深入。

**每个文件夹内的 `README.md` 不需要写长篇笔记**，只放三样东西：
1. 该模块在官方教程中的对应链接；
2. 一句话说明这个模块解决了什么问题；
3. 本次练习中你跑通的关键输出或结论（例如：FashionMNIST 的 batch shape 是 `[64, 1, 28, 28]`）。

**notebook 文件直接用官方提供的可下载版本**，在本地运行后保留输出结果。官方教程的代码可以直接在 Colab 运行，下载 `.ipynb` 放到对应文件夹即可，不需要自己从头抄写，把精力放在理解和修改实验上。

### 根目录文件的作用

`requirements.txt` 固定你运行时的版本，避免日后环境变化导致 notebook 跑不通。内容至少包含：
```text
torch
torchvision
```
如果用到 notebook 可视化，可以加上 `matplotlib`。不需要写死具体版本号，除非你发现某个版本有兼容问题。

`.gitignore` 至少忽略 `data/` 目录，因为 FashionMNIST 等数据集下载后会占用空间，不应该提交到仓库。

`README.md` 作为仓库首页，放一张学习进度表即可：

| 模块 | 状态 | 完成日期 | 关键收获 |
|---|---|---|---|
| Quickstart | ✅ | | 跑通了完整训练循环 |
| Tensors | ✅ | | 理解了 shape 和 device |
| ... | | | |

### 为什么不按“天”或“周”分文件夹

培训班常见做法是 `day01/`、`week1/`，但跟随官方教程自学时，**按知识模块分文件夹比按时间分更可持续**。你某天可能只看了 Tensors，另一天把 Datasets 和 Transforms 一起看了，按模块组织不会让内容归属变得尴尬。日后回顾时，想查 “Autograd 我当时怎么理解的”，直接进 `05_autograd/` 就行，不需要回忆那是第几天学的。
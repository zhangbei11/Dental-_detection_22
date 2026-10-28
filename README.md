# Dental Detection

## 数据集准备

数据集建议采用以下目录结构：

```text
New_datasets_23/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

标注文件使用 YOLO 格式，每行内容为：

```text
class_id x_center y_center width height
```

坐标和宽高均应归一化到 `0–1`。训练前，请在
[`ultralytics/cfg/datasets/tooth_oral22.yaml`](ultralytics/cfg/datasets/tooth_oral22.yaml)
中把 `path` 修改为本机数据集的绝对路径。

## 模型训练

当前训练入口为 [`train.py`](train.py)。运行前需要修改以下三处服务器路径：

- RT-DETR 模型配置路径
- 数据集配置路径
- 训练结果输出路径 `project`

完成修改后运行：

```bash
python train.py
```

默认训练参数：

| 参数 | 默认值 |
| --- | ---: |
| 输入尺寸 | 640 |
| 训练轮数 | 100 |
| 批次大小 | 8 |
| 数据加载线程 | 4 |
| 实验名称 | `1027-baseline` |

如需断点续训，可在 `train.py` 中设置：

```python
resume="runs/train-22/1027-baseline/weights/last.pt"
```

## 模型预测

使用基线最佳权重进行预测：

```bash
yolo predict \
  model=runs/train-22/1027-baseline/weights/best.pt \
  source=/path/to/image-or-directory \
  imgsz=640 \
  save=True
```

也可以在 Python 中调用：

```python
from ultralytics import RTDETR

model = RTDETR("runs/train-22/1027-baseline/weights/best.pt")
results = model.predict(source="/path/to/image.jpg", imgsz=640, save=True)
```

## 基线模型

基线实验位于 [`runs/train-22/1027-baseline`](runs/train-22/1027-baseline)：

- `weights/best.pt`：验证集表现最佳的权重，推荐用于预测和部署
- `weights/last.pt`：最后一个训练轮次的权重，主要用于断点续训
- `results.csv`：逐轮训练指标
- `results.png`：训练指标曲线
- `confusion_matrix*.png`：混淆矩阵
- `Box*_curve.png`：精确率、召回率和 F1 等评估曲线

## 检测类别

| ID | Class | 中文说明 |
| ---: | --- | --- |
| 0 | Apical Periodontitis | 根尖周炎 |
| 1 | Decay | 龋齿 |
| 2 | Wisdom Tooth | 智齿 |
| 3 | Missing Tooth | 缺失牙 |
| 4 | Dental Filling | 牙体充填物 |
| 5 | Root Canal Filling | 根管充填物 |
| 6 | Implant | 种植体 |
| 7 | Porcelain Crown | 烤瓷冠 |
| 8 | Ceramic Bridge | 陶瓷桥 |
| 9 | Bracket | 托槽 |
| 10 | Coronal Destruction | 牙冠破坏 |
| 11 | Ceramic Bracket | 陶瓷托槽 |
| 12 | Malocclusion | 错颌畸形 |
| 13 | Hyperdontia | 多生牙 |
| 14 | Edentulism | 牙列缺失 |
| 15 | Titanium Plate | 钛板 |
| 16 | Metallic Foreign Body | 金属异物 |
| 17 | Space Maintainer | 间隙保持器 |
| 18 | Transpalatal Arch | 腭弓 |
| 19 | Impacted Tooth | 阻生牙 |
| 20 | Denture Metal | 金属义齿 |
| 21 | Metallic Attachment | 金属附件 |


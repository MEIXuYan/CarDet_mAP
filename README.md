# 交通数据集检测效果分析

## 实现功能
基于mAP代码的精度计算代码：
* label文件读取和转码
* [mAP](https://github.com/Cartucho/mAP)精度计算

## 运行方法
Python顺序运行以下代码：

```
python data_scripts/convert_dataset.py
python data_scripts/convert_gt2txt.py
python data_scripts/convert_pred2txt.py
python main.py
```
# 交通数据集检测效果分析

## 实现功能
基于mAP代码的精度计算代码：
* label文件读取和转码
* [mAP](https://github.com/Cartucho/mAP)精度计算

## 运行方法
Python顺序运行以下代码：

多类别精度计算：
```
python data_scripts/convert_dataset.py
python data_scripts/convert_gt2txt.py
python data_scripts/convert_pred2txt.py
python mAP.py
```

Car类别精度分距离计算：
```
python data_scripts/convert_gt2txt_car.py
python data_scripts/convert_pred2txt_car.py
python mAP_car.py
```
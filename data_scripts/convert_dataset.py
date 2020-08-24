# DIDI Car Detection Analysis
# Author: Xu Yan
# 2020.08.23

# 功能实现：
# 1 读入txt的预测结果，txt内容转码
# 2 对比json文件的GT结果，计算IoU、AP、mAP指标
# 3 分距离（像素y坐标值或其他指标）测算精度，绘制曲线

import os
import sys
import numpy
import json
import glob
import math
import shutil
import operator

# data input 
TXT_PATH = './dataset53/txt/'
JSON_PATH = './dataset53/json/'
JPG_PATH = './dataset53/jpg/'
# data output
PD_PATH = './dataset53/pred/'
GT_PATH = './dataset53/gt/'
IMG_PATH = './input/images-optional/'
file_list = []

# dir
if not os.path.exists(PD_PATH): 
    os.makedirs(PD_PATH)
if not os.path.exists(GT_PATH): 
    os.makedirs(GT_PATH)
if not os.path.exists(IMG_PATH): 
    os.makedirs(IMG_PATH)

# file list 
for dirpath, dirnames, files in os.walk(JSON_PATH):
    file_list= [x.split(".json",1)[0] for x in files]

# file list
for file_name in file_list:
    #
    txts = TXT_PATH + file_name + '.txt'
    txtd = PD_PATH + file_name + '.json'
    jsons = JSON_PATH + file_name + '.json'
    jsond = GT_PATH + file_name + '.json'
    jpgs = JPG_PATH + file_name + '.jpg'
    jpgd = IMG_PATH + file_name + '.jpg'
    # 
    shutil.copy2(txts, txtd)
    shutil.copy2(jsons, jsond)
    shutil.copy2(jpgs, jpgd)

    #print (file_name)




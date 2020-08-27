# convert json to txt
# XuYan 2020.08.24
import sys
import os
import glob
import json

def get_range(center_y):
  if center_y < 120:
    class_name = 'car_1'
  elif center_y < 240:
    class_name = 'car_2'
  elif center_y < 360:
    class_name = 'car_3'
  else:
    class_name = 'car_4'
  return class_name 

# 
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN_PATH = BASE_PATH + '/dataset53/gt/'
OUT_PATH = BASE_PATH + '/input_car/ground-truth/'
file_list = []
class_list = []

#
if not os.path.exists(OUT_PATH): 
    os.makedirs(OUT_PATH)

#
for dirpath, dirnames, files in os.walk(IN_PATH):
    file_list = [x.split(".json",1)[0] for x in files]
#print(file_list)

#
for file_name in file_list:
  #print(tmp_file)
  # 1. create new file (VOC format)
  dst = open(OUT_PATH + file_name + '.txt', 'w')
  data = json.load(open(IN_PATH + file_name + '.json'))
  data = data['shapes']
  for obj in data:
    obj_name = obj['label']
    if obj_name == 'car':
      left = obj['points'][0][0]
      top = obj['points'][0][1]
      right = obj['points'][1][0]
      bottom = obj['points'][1][1]

      # get class name
      # car bicycle truck pedestrian
      # car person pedestrian bicycle truck motorbike bicylcle
      if obj_name not in class_list:
        print(obj_name)
        class_list.append(obj_name)
      if obj_name in ['bicycle', 'motorbike', 'bicylcle']:
        obj_name = 'bicycle'
      if obj_name in ['person', 'pedestrian']:
        obj_name = 'pedestrian'
      
      # order check
      # make sure left < right / top < bottom
      if float(left) > float(right):
        right,left = left,right
      if float(top) > float(bottom):
        top,bottom = bottom,top
      
      # int data
      left, top, right, bottom = int(float(left)), int(float(top)), int(float(right)), int(float(bottom))
      center_y = (top + bottom)/2
      obj_name = get_range(center_y)
      dst.write(obj_name + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')

print("Conversion completed!")

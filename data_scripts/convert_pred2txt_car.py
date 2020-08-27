# convert json to txt
# XuYan 2020.08.24
import sys
import os
import glob
import json

def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):
  ## remove normalization given the size of the image
  x_c = float(x_c_n) * img_width
  y_c = float(y_c_n) * img_height
  width = float(width_n) * img_width
  height = float(height_n) * img_height
  ## compute half width and half height
  half_width = width / 2
  half_height = height / 2
  ## compute left, top, right, bottom
  ## in the official VOC challenge the top-left pixel in the image has coordinates (1;1)
  left = int(x_c - half_width) + 1
  top = int(y_c - half_height) + 1
  right = int(x_c + half_width) + 1
  bottom = int(y_c + half_height) + 1
  return left, top, right, bottom


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
IN_PATH = BASE_PATH + '/dataset53/pred/'
OUT_PATH = BASE_PATH + '/input_car/detection-results/'
file_list = []
class_list = []

#
if not os.path.exists(OUT_PATH): 
    os.makedirs(OUT_PATH)

# 
for dirpath, dirnames, files in os.walk(IN_PATH):
    file_list = [x.split(".json",1)[0] for x in files]
#print(file_list)

for file_name in file_list:
  dst = open(OUT_PATH + file_name + '.txt', 'w')
  data = json.load(open(IN_PATH + file_name + '.json'))
  data = data['objs']
  for obj in data:
    obj_name = obj['type']
    if obj_name == 'car':
      conf = obj['type_confidence']
      x_c_n = obj['bbox_centre_x']
      y_c_n = obj['bbox_centre_y']
      width_n = obj['bbox_size_x']
      height_n = obj['bbox_size_y']
      img_width = 640
      img_height = 480
      
      # get class name
      # car bicycle truck pedestrian
      if obj_name not in class_list:
        print(obj_name)
        class_list.append(obj_name)
      
      # convert coordinates
      left, top, right, bottom = convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height)
      center_y = (top + bottom)/2
      obj_name = get_range(center_y)
      
      dst.write(obj_name + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')

print("Conversion completed!")

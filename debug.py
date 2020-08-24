# debug and visualization
import sys,os
from cv2 import cv2
import matplotlib

def file_lines_to_list(path):
    # open txt file lines to a list
    with open(path) as f:
        content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

GT_PATH = os.path.join(os.getcwd(), 'input', 'ground-truth/')
DR_PATH = os.path.join(os.getcwd(), 'input', 'detection-results/')
IMG_PATH = os.path.join(os.getcwd(), 'input', 'images-optional/')
file_name = '1590892643175'

gt = file_lines_to_list(GT_PATH + file_name + '.txt')
pred = file_lines_to_list(DR_PATH + file_name + '.txt')
img = cv2.imread(IMG_PATH + file_name + '.jpg')

for line in gt:
    typename, x1, y1, x2, y2 = line.split()
    x1, y1, x2, y2 = int(float(x1)), int(float(y1)), int(float(x2)), int(float(y2))
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)

for line in pred:
    typename, confi, x1, y1, x2, y2 = line.split()
    x1, y1, x2, y2 = int(float(x1)), int(float(y1)), int(float(x2)), int(float(y2))
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

cv2.imshow('FRAME', img)
cv2.waitKey(2000)



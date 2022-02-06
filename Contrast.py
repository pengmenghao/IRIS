"""
 作者：pengmenghao
 日期：2021年7月13日
 """
import cv2
from function.contrast import contrast

test_img_path = './photo/4/R/1.jpeg'
test_img = cv2.imread(test_img_path, 0)
name, side, scores = contrast(test_img)

print(name)
print(side)
print(scores)
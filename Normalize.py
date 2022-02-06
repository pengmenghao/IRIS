"""
 作者：pengmenghao
 日期：2021年7月13日
 """
from IOCircle import outer, inner
from function.normalize import normalize
import cv2
import matplotlib.pyplot as plt


# 成比例调节
height = 40
width = 512

img_path = './photo/5/L/1.jpeg'
img = cv2.imread(img_path, 0)
polar_array, polar_noise = normalize(img, outer[0], outer[1], outer[2], inner[0], inner[1], inner[2], height, width)
plt.imshow(polar_array, cmap='gray')
plt.show()
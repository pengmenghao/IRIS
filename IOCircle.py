"""
 作者：pengmenghao
 日期：2021年7月13日
 """
import cv2
import matplotlib.pyplot as plt
from function.innerCircle import innerCircle
from function.outerCircle import outerCircle
from function.visualization import displayCircle

img_path = './photo/5/L/1.jpeg'
img = cv2.imread(img_path, 0)
inner = innerCircle(img)
outer = outerCircle(img, inner)
cimg = displayCircle(img, outer[0], outer[1], outer[2], inner[0], inner[1], inner[2])
plt.imshow(cimg)
plt.show()


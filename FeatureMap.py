"""
 作者：pengmenghao
 日期：2021年7月13日
 """
import cv2
from function.feature import getFeatureMap
import matplotlib.pyplot as plt


feature = getFeatureMap(cv2.imread("./photo/1/L/1.jpeg", 0), 'swt')
plt.imshow(feature, cmap='gray')
plt.show()


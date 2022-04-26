# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:09:32 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:53:16 2018

@author: lenovo
"""

import cv2
import numpy as np

'''
轮廓检测
'''

#加载图像img
img = cv2.imread('/home/huangfu/桌面/face/airplane.jpg',cv2.IMREAD_COLOR)
cv2.imshow('img',img)


#转换为灰色gray_img
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_img',gray_img)


#对图像二值化处理 输入图像必须为单通道8位或32位浮点型
ret,thresh = cv2.threshold(gray_img,127,255,0)
cv2.imshow('thresh',thresh)



#寻找图像轮廓 返回修改后的图像 图像的轮廓  以及它们的层次
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('image',image)
print('contours[0]:',contours[0])
print('len(contours)',len(contours))
print('hierarchy,shape',hierarchy.shape)
print('hierarchy[0]:',hierarchy[0])


#在原图img上绘制轮廓contours
img = cv2.drawContours(img,contours,-1,(0,255,0),2)
cv2.imshow('contours',img)

        
cv2.waitKey()
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:09:32 2018

@author: lenovo
"""

'''
SURF算法
'''
import cv2
import numpy as np

img = cv2.imread('/home/huangfu/桌面/face/people.jpeg')
img = cv2.resize(img,dsize=(1500,1000))
#转换为灰度图像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#创建一个SURF对象
surf = cv2.xfeatures2d.SURF_create(20000)
#SURF对象会使用Hessian算法检测关键点，并且对每个关键点周围的区域计算特征向量。该函数返回关键点的信息和描述符
keypoints,descriptor = surf.detectAndCompute(gray,None)
print(type(keypoints),len(keypoints),keypoints[0])
print(descriptor.shape)
#在图像上绘制关键点
#img = cv2.drawKeypoints(image=img,keypoints = keypoints,outImage=img,color=(255,0,255),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img = cv2.drawKeypoints(image=img,keypoints = keypoints,outImage=img,color=(255,0,255),flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
# image:也就是原始图片
# keypoints：从原图中获得的关键点，这也是画图时所用到的数据
# outputimage：输出              //可以是原始图片 
# color：颜色设置，通过修改（b,g,r）的值,更改画笔的颜色，b=蓝色，g=绿色，r=红色。
# flags：绘图功能的标识设置

# flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT 默认参数,仅仅画出了圆的中心点
# flags=cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG：不创建输出图像矩阵，而是在输出图像上绘制匹配对
# flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 对每一个特征点绘制带大小和方向的关键点图形
# flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS：单点的特征点不被绘制 

#显示图像
cv2.imshow('surf_keypoints',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

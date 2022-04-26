#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Saturday June 29 10:09:02 2019
@author: Damon

"""
import cv2
import random
import os
import os.path
import pandas as pd
import numpy  as np
from copy import deepcopy
from skimage import io

#文件的开头
index = 0
step = 200
slide_x1 = 0
slide_y1 = 0
datPath = '/home/huangfu/桌面/dat/'
imagePath = '/home/huangfu/桌面/图片/'
saveImagePath = '/home/huangfu/样本/'

# 每两个检测框框是否有交叉，如果有交集则返回重叠度 IOU, 如果没有交集则返回 0
def area_overlab(x1, y1, w1, h1, data):
    overlapRate = [0]
    for j in range(len(data)):
        x2 = data.values[j][0]
        y2 = data.values[j][1]
        w2 = data.values[j][2]
        h2 = data.values[j][3]

        if(x1>x2+w2):
            continue
        if(y1>y2+h2):
            continue
        if(x1+w1<x2):
            continue
        if(y1+h1<y2):
            continue
        colInt = abs(min(x1 +w1 ,x2+w2) - max(x1, x2))
        rowInt = abs(min(y1 + h1, y2 +h2) - max(y1, y2))
        overlap_area = colInt * rowInt
        area1 = w1 * h1
        area2 = w2 * h2
        #overlapRate 计算得出的重叠率
        if(overlap_area / area2 > 0):
            overlapRate.append(overlap_area / area2)

    return overlapRate

for root, dirs, files in os.walk(imagePath):
    #获取文件的名称
    for file in files:
        try:
            iFile = file.split(".")[0]
            #print(iFile)
            uImagePath = imagePath + iFile + '.tif'
            iDatPath = datPath + iFile + '.dat';
            img = cv2.imdecode(np.fromfile(uImagePath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            data = pd.read_csv(iDatPath,header=None,skiprows=[0],sep='\s+')
            # 在图片里滑动截图
            # 在图片里滑动截图
            while (slide_y1 + step < img.shape[0]):
                slide_x1 = 0
                while (slide_x1 + step < img.shape[1]):
                    overlapRate = area_overlab(slide_x1, slide_y1, step, step, data)

                    if max(overlapRate) == 0:
                        cropped = img[slide_y1 : slide_y1 + step, slide_x1 : slide_x1 + step]
                        imgPath_1 = saveImagePath + str(index).zfill(6) + '.jpg'
                        index += 1
                        print(str(index)+'.jpg')
                        cv2.imwrite(imgPath_1,cropped)
                    slide_x1 += step
                slide_y1 += step

            #每张图片读取完，初始化参数
            slide_y1 = 0
            slide_x1 = 0
        except:
            print('不存在对应的.dat文件')



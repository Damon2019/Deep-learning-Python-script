#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:03:02 2019
@author: Administrator

"""
import cv2
import random
import os
import os.path
import pandas as pd
import numpy  as np
from copy import deepcopy

index = 1
picNumber = 0
datPath = '/home/huangfu/objectDetection/mAP/path/dat/'
txtPath = '/home/huangfu/桌面/Partial/123.txt'
imagePath = '/home/huangfu/桌面/Partial/0ship-jpg/'
xmlPath = '/home/huangfu/桌面/Partial/ship-xml/'
saveXmlPath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/Annotations/'
saveImagePath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/JPEGImages/'

for root, dirs, files in os.walk(datPath):
    #获取文件的名称 000001
    for file in files:
#data = pd.read_csv(txtPath,header=None,skiprows=[0],sep='\s+')
        iFile = file.split(".")[0]
        data = pd.read_csv(datPath+file,header=None,skiprows=[0],sep='\s+')
        for i in range(len(data)):
            data.values[i][4] = 1
        data.to_csv('/home/huangfu/objectDetection/mAP/path/dat1/'+iFile+'.dat',sep=' ')
        index += 1






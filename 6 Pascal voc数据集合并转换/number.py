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

index = 10072
picNumber = 0
txtPath = '/home/huangfu/桌面/Partial/Air.txt'
imagePath = '/home/huangfu/桌面/Partial/0ship-jpg/'
xmlPath = '/home/huangfu/桌面/Partial/Air-xml/'
saveXmlPath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/Annotations/'
saveImagePath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/JPEGImages/'

for root, dirs, files in os.walk(imagePath):
    #print('files:', files)  # 当前路径下所有非目录子文件
    #print('tyoe files:',type(files))

    #获取文件的名称 000001
    for file in files:
        iFile = file.split(".")[0]
        fpTxt = open('/home/huangfu/桌面/Partial/123.txt','a+')
        fpTxt.writelines(str(iFile).zfill(8) + '\n')
        fpTxt.close()


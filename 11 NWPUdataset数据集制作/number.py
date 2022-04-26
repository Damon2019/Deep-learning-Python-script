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

imagePath = '/home/huangfu/桌面/NWPUdataset/groundTruth/'
saveImagePath = '/home/huangfu/桌面/NWPUdataset/n/'

for root, dirs, files in os.walk(imagePath):
    #print('files:', files)  # 当前路径下所有非目录子文件
    #print('tyoe files:',type(files))

    #获取文件的名称 000001
    for file in files:
        print(file)
        iFile = file.split(".")[0]
        img = cv2.imread(imagePath + file)
        cv2.imwrite(saveImagePath + str(int(iFile)+index) +'.jpg',img)



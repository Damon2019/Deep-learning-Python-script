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
change_txt = 1
datPath = '/home/huangfu/objectDetection/mAP/path/dat/'

for root, dirs, files in os.walk(datPath):
    #获取文件的名称 000001
    for file in files:
#data = pd.read_csv(txtPath,header=None,skiprows=[0],sep='\s+')
        iFile = file.split(".")[0]
        data = pd.read_csv(datPath+file,header=None,skiprows=[0],sep='\s+')
        for i in range(len(data)):
            data.values[i][4] = change_txt
        data.to_csv('/home/huangfu/objectDetection/mAP/path/dat1/'+iFile+'.dat',sep=' ')
        index += 1






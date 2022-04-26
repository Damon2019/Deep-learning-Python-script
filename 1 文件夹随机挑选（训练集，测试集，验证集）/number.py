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

imagePath = 'train/'
txtSavePath = ''

for root, dirs, files in os.walk(imagePath):
    #print('files:', files)  # 当前路径下所有非目录子文件
    #print('tyoe files:',type(files))

    #获取文件的名称 000001
    # os.mknod(txtSavePath + "train.txt") #创建空文件
    for file in files:
        iFile = file.split(".")[0]
        fpTxt = open(txtSavePath + 'train.txt','a+')
        fpTxt.writelines(str(iFile).zfill(6) + '\n')
        fpTxt.close()


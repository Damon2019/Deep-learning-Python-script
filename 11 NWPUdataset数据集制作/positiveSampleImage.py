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
datPath = '/home/huangfu/桌面/dat/'
imagePath = '/home/huangfu/桌面/图片/'
saveImagePath = '/home/huangfu/样本/'

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
            for i in range(len(data)):
                # cut image
                '''
                if data.values[i][2] < 150 or data.values[i][3] < 150:
                    continue
                '''
                dim = (200, 200)
                cropped = img[data.values[i][1] : data.values[i][1] + data.values[i][3], data.values[i][0] : data.values[i][0] + data.values[i][2]]
                resized = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
                imgPath_1 = saveImagePath + str(index).zfill(6) + '.jpg'
                cv2.imwrite(imgPath_1,resized)
                index += 1

            #每张图片读取完，初始化参数
            slide_y1 = 0
            slide_x1 = 0
            #cv2.waitKey (0)
            #cv2.destroyAllWindows()
            #cv2.imwrite('/home/huangfu/桌面/'+file, img)
        except:
            print('不存在对应的.dat文件')

#xml_name(datPath)


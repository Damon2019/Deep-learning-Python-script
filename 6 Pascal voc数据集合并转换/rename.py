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

index = 72831
picNumber = 0
txtPath = '/home/huangfu/桌面/Partial/123.txt'
imagePath = '/home/huangfu/桌面/Partial/0ship-jpg/'
xmlPath = '/home/huangfu/桌面/Partial/ship-xml/'
saveXmlPath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/Annotations/'
saveImagePath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/JPEGImages/'

#data = pd.read_csv(txtPath,header=None,skiprows=[0],sep='\s+')
data = pd.read_csv(txtPath,header=None,sep='\s+')
for i in range(len(data)):
    try:
        number = data.values[i][0]
        #print(number)

        bPicName = str(number).zfill(8) + '.jpg'
        aPicName = str(number + index).zfill(8) + '.jpg'
        bXmlName = str(number).zfill(8) + '.xml'
        aXmlName = str(number + index).zfill(8) + '.xml'

        # 查找图片
        img = cv2.imread(imagePath + bPicName)
        cv2.imwrite(saveImagePath + aPicName,img)

        # xml操作
        fp = open(xmlPath + bXmlName,'r')
        fp1 = open(saveXmlPath + aXmlName,'w')
        for i in fp:
            fp1.write(i)                        #向新文件中写入数据
        fp.close()
        fp1.close()

        fpTxt = open('/home/huangfu/VOC2007/VOCdevkit/VOC2007/ship.txt','a+')
        fpTxt.writelines(str(number + index).zfill(8) + '\n')
        fpTxt.close()
    except:
        print('没有对应的')






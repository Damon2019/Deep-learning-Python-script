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
txtPath = '/home/huangfu/objectDetection/数据集合并转换/picall.txt'

imagePath = '/home/huangfu/桌面/Partial/Air-img/'
xmlPath = '/home/huangfu/桌面/Partial/Air-xml/'
saveXmlPath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/Annotations/'
saveImagePath = '/home/huangfu/VOC2007/VOCdevkit/VOC2007/JPEGImages/'


with open(txtPath, 'r') as f:
    for line in f:
        print(line)


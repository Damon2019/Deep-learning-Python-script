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

index = 000000
picNumber = 0
folder_pic = '11/'

save_filePath = 'pic/'


xmlPath = '11/'
saveXmlPath = 'xml/'


file_names = os.listdir(folder_pic)
file_names.sort(key=lambda x: int(x.split('.')[0]))#按照数字进行排序后按顺序读取文件夹下的图片

for name in file_names:
    # print(name)
    old_filename_pic = name.split('.')[0]
    # new_filename = int(old_filename) - index
    new_filename_pic = index

    old_filename_xml = name.split('.')[0]
    new_filename_xml = index

    # image操作
    old_filename_picpath = folder_pic + old_filename_pic + '.jpg'
    new_filename_picpath = save_filePath + str(new_filename_pic).zfill(6) + '.jpg'
    # xml 操作
    old_filename_xmlpath = xmlPath + old_filename_xml + '.xml'
    new_filename_xmlpath = saveXmlPath + str(new_filename_xml).zfill(6) + '.xml'

    if os.path.exists(old_filename_picpath):
        if os.path.exists(old_filename_xmlpath):
            os.rename(old_filename_picpath, new_filename_picpath)
            os.rename(old_filename_xmlpath, new_filename_xmlpath)
            index += 1



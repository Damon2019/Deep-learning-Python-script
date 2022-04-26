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

folder_pic = 'jpg/'

save_filePath = 'JPEGImages/'


xmlPath = 'xml/'
saveXmlPath = 'Annotations/'


file_names = os.listdir(folder_pic)

for name in file_names:
    # print(name)

    # image操作
    old_filename_picpath = folder_pic + name.split('.')[0] + '.jpg'
    new_filename_picpath = save_filePath + name.split('.')[0] + '.jpg'
    # xml 操作
    old_filename_xmlpath = xmlPath + name.split('.')[0] + '.xml'
    new_filename_xmlpath = saveXmlPath + name.split('.')[0] + '.xml'

    if os.path.exists(old_filename_picpath):
        if os.path.exists(old_filename_xmlpath):
            os.rename(old_filename_picpath, new_filename_picpath)
            os.rename(old_filename_xmlpath, new_filename_xmlpath)



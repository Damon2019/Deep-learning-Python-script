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

# index = 100180
index = 000000
picNumber = 0
folder_pic = '/home/huangfu/9.7/test3/'

save_filePath = '/home/huangfu/9.7/xml/'


xmlPath = '/home/huangfu/9.7/ship-cut-jpg/'
saveXmlPath = '/home/huangfu/9.7/pic/'

xmlPath1 = '/home/huangfu/9.7/ship-cut-xml/'
saveXmlPath1 = '/home/huangfu/9.7/pic1/'


file_names = os.listdir(folder_pic)

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
    old_filename_xmlpath = xmlPath + old_filename_xml + '.jpg'
    new_filename_xmlpath = saveXmlPath + str(new_filename_xml).zfill(6) + '.jpg'


    old_filename_xmlpath1 = xmlPath1 + old_filename_xml + '.xml'
    new_filename_xmlpath1 = saveXmlPath1 + str(new_filename_xml).zfill(6) + '.xml'

    if os.path.exists(old_filename_picpath):
        if os.path.exists(old_filename_xmlpath):
            if os.path.exists(old_filename_xmlpath1):
                os.rename(old_filename_picpath, new_filename_picpath)
                os.rename(old_filename_xmlpath, new_filename_xmlpath)
                os.rename(old_filename_xmlpath1, new_filename_xmlpath1)
                index += 1



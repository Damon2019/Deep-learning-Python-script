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
import shutil

folder_pic = './show/'

pic_path = './pic/'
xml_path = './xml/'

pic_paths = './pic1/'
xml_paths = './xml1/'



file_names = os.listdir(folder_pic)

for name in file_names:
    # image操作
    #old_filename_picpath1 = folder_pic + name.split('.')[0] + '.jpg'
    pic_path_del = pic_path + name.split('.')[0] + '.jpg'
    xml_path_del = xml_path + name.split('.')[0] + '.xml'

    pic_path_del_save = pic_paths + name.split('.')[0] + '.jpg'
    xml_path_del_save = xml_paths + name.split('.')[0] + '.xml'
    
    if os.path.exists(pic_path_del):
        if os.path.exists(xml_path_del):
            os.rename(pic_path_del, pic_path_del_save)
            os.rename(xml_path_del, xml_path_del_save)





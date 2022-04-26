#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Saturday June 29 10:09:02 2019
@author: Damon

"""
import cv2
import os
import os.path
import pandas as pd
import numpy  as np

datPath = './1/'

if __name__ == '__main__':
    for root, dirs, files in os.walk(datPath):
        print(root,dirs,files)
        for fileName in files:
            try:
                iDatPath = datPath + fileName;
                data = pd.read_csv(iDatPath, header=None, skiprows=[0], sep='\s+')
                for j in range(len(data)):
                    x2 = data.values[j][0]
                    y2 = data.values[j][1]
                    w2 = data.values[j][2]
                    h2 = data.values[j][3]
                    print('x2:', x2, 'y2:',y2,'w2:', w2, 'h2:',h2)
                    if x2 < 0 or y2 < 0 or w2 < 0 or h2 < 0:
                      print('error:', str(fileName))
            except:
                print('error dat:', str(fileName))


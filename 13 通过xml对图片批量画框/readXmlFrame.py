#!/usr/bin/env python3
#coding=utf-8
import os
import os.path
import xml.dom.minidom
import cv2
#import pandas as pd
import numpy  as np
import time
xmlPath = './2/'
imagePath = './1/'
saveImagePath = './save/'
def xml_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print('root_dir:', root)  # 当前目录路径
        #print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
        print('tyoe files:',type(files))

        
        #获取文件的名称 000001
        for file in files:
            iFile = file.split(".")[0]
            #print(iFile)
            uImagePath = imagePath + iFile + '.jpg'
            uSaveImagePath = saveImagePath + iFile + '.jpg'
            print(uImagePath)
            #xml读取操作，将获取到的xml文件名送入到dom中解析
            iXmlPath = xmlPath + file;
            DomTree = xml.dom.minidom.parse(iXmlPath)
            annotation = DomTree.documentElement


            objectlist = annotation.getElementsByTagName('object')
            #print('objectlist',objectlist)
            #画框
            img = cv2.imread(uImagePath)
            print(img.shape)
            for objects in objectlist:   # print objects
                nameList = objects.getElementsByTagName('name')
                objectname=nameList[0].childNodes[0].data
                #print('name : ',objectname)

                bndbox = objects.getElementsByTagName('bndbox')
                cropboxes = []
                for box in bndbox:
                    try:
                        x1_list = box.getElementsByTagName('xmin')
                        x1 = int(x1_list[0].childNodes[0].data)
                        y1_list = box.getElementsByTagName('ymin')
                        y1 = int(y1_list[0].childNodes[0].data)
                        x2_list = box.getElementsByTagName('xmax')
                        x2 = int(x2_list[0].childNodes[0].data)
                        y2_list = box.getElementsByTagName('ymax')
                        y2 = int(y2_list[0].childNodes[0].data)
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)


                    except Exception as e:
                        print(e)
            #cv2.waitKey (0)
            #cv2.destroyAllWindows()
            cv2.imwrite(uSaveImagePath, img)
            #time.sleep(2)


xml_name(xmlPath)


# -*- coding: utf-8 -*-
from lxml.etree import Element,SubElement,tostring
from xml.dom.minidom import parseString
import xml.dom.minidom
import os
import sys
from PIL import Image
import cv2

#把txt中的内容写进xml
def deal(path, path1):
    files=os.listdir(path)#列出所有文件
    for file in files:
        filename=os.path.splitext(file)[0]#分割出文件名
        #print(filename)
        sufix=os.path.splitext(file)[1]#分割出后缀
        if sufix=='.jpg':
            img = cv2.imread(path + '/' + file)
            #写入VocXml
            node_root = Element('annotation')

            node_folder = SubElement(node_root, 'folder')
            node_folder.text = 'VOC2007'

            node_filename = SubElement(node_root, 'filename')
            node_filename.text = str(filename).zfill(6) + '.jpg'

            node_filename = SubElement(node_root, 'path')
            node_filename.text = path + '/' + str(filename).zfill(6) + '.jpg'

            node_source = SubElement(node_root, 'source')
            node_database = SubElement(node_source, 'database')
            node_database.text = 'UnKnown'

            node_size = SubElement(node_root, 'size')
            node_width = SubElement(node_size, 'width')
            node_width.text = str(img.shape[1])
            node_height = SubElement(node_size, 'height')
            node_height.text = str(img.shape[0])
            node_depth = SubElement(node_size, 'depth')
            node_depth.text = '3'

            node_segmented = SubElement(node_root, 'segmented')
            node_segmented.text = '0'

            xml = tostring(node_root)  #格式化显示
            dom = parseString(xml)

            #写入voc格式xml文件
            xml_name = os.path.join(path1, str(filename).zfill(6) + '.xml')
            with open(xml_name, 'wb') as f:
                f.write(dom.toprettyxml(indent='\t', encoding='utf-8'))



if __name__ == "__main__":
    path=('/home/huangfu/桌面/NWPUdataset/groundTruth')
    path1=('/home/huangfu/桌面/NWPUdataset/n/')
    deal(path, path1)



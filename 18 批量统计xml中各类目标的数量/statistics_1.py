# -*- coding:utf-8 -*-
# nansbas
# 2019.1.21
import os
import sys
import xml.etree.ElementTree as ET
import numpy as np
np.set_printoptions(suppress=True, threshold=sys.maxsize)
import matplotlib
from PIL import Image

if __name__ == '__main__':
    size = 200
    number = 0

    xml_path='xml1/'
    filenames = os.listdir(xml_path)

    for name in filenames:
        tree=ET.parse(xml_path + name)
        root=tree.getroot()
        for obj in tree.findall('object'):
            obj_struct={}
            obj_struct['name']=obj.find('name').text
            bbox=obj.find('bndbox')
            obj_struct['bbox']=[int(bbox.find('xmin').text),
                               int(bbox.find('ymin').text),
                               int(bbox.find('xmax').text),
                               int(bbox.find('ymax').text)]
            ob_w = int(bbox.find('xmax').text) - int(bbox.find('xmin').text)
            ob_h = int(bbox.find('ymax').text) - int(bbox.find('ymin').text)
            ob_area = ob_w*ob_h

            if ob_area < size:
                number += 1

    # print("min_value: ", min_value)
    # list_all.sort()
    # print("list_all: ", list_all)
    print("number: ", number)

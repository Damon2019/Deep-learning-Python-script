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
def parse_obj(xml_path, filename):
  tree=ET.parse(xml_path+filename)
  objects=[]
  for obj in tree.findall('object'):
    obj_struct={}
    obj_struct['name']=obj.find('name').text
    bbox=obj.find('bndbox')
    obj_struct['bbox']=[int(bbox.find('xmin').text),
                        int(bbox.find('ymin').text),
                         int(bbox.find('xmax').text),
                        int(bbox.find('ymax').text)]
    objects.append(obj_struct)
  return objects
def read_image(image_path, filename):
  im=Image.open(image_path+filename)
  W=im.size[0]
  H=im.size[1]
  area=W*H
  im_info=[W,H,area]
  return im_info
 
 
if __name__ == '__main__':
  image_path='/home/huangfu/objectDetection/1-深度学习代码/19 批量删除xml中过小的目标/voc_ship_v3/VOC2007/JPEGImages/'
  xml_path='/home/huangfu/objectDetection/1-深度学习代码/19 批量删除xml中过小的目标/voc_ship_v3/VOC2007/Annotations/'
  filenamess=os.listdir(xml_path)
  xml_path2='/home/huangfu/objectDetection/1-深度学习代码/19 批量删除xml中过小的目标/voc_ship_v3/VOC2007/Annotations1/'
  filenames=[]
  for name in filenamess:
    name=name.replace('.xml','')
    filenames.append(name)
  recs={}
  ims_info={}
  obs_shape={}
  classnames=[]
  num_objs={}
  obj_avg={}
 
  for name in filenames:
    tree=ET.parse(xml_path+name+ '.xml')
    root=tree.getroot()
    objects=[]
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
           if ob_area<=961:
             print("这个图片目标过小:{},{}".format(name,object))
             root.remove(obj)
             print("已删除")
    tree.write(xml_path2+ name+ '.xml')

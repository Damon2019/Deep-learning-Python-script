# -*- coding: utf-8 -*-
#import sys;
#reload(sys);
#sys.setdefaultencoding('utf8')
import cv2
import os
import xml.dom.minidom

def modify_xml(filename):
    newwidth = x_size
    newheight = y_size
    xmlfile = filename.split('.')[0] + '.xml'
    DOMTree = xml.dom.minidom.parse(os.path.join(dir_xml, xmlfile))
    collection = DOMTree.documentElement
    for width in collection.getElementsByTagName("width"):
        oldwidth = int(width.firstChild.data)
        width.firstChild.data = str(newwidth)
    for height in collection.getElementsByTagName("height"):
        oldheight = int(height.firstChild.data)
        height.firstChild.data = str(newheight)
    for xmin in collection.getElementsByTagName("xmin"):
        xmin.firstChild.data = int(int(xmin.firstChild.data) / 1.0 / oldwidth* newwidth)
    for xmax in collection.getElementsByTagName("xmax"):
        xmax.firstChild.data = int(int(xmax.firstChild.data) / 1.0 / oldwidth * newwidth)
    for ymin in collection.getElementsByTagName("ymin"):
        ymin.firstChild.data = int(int(ymin.firstChild.data) / 1.0 / oldheight * newheight)
    for ymax in collection.getElementsByTagName("ymax"):
        ymax.firstChild.data = int(int(ymax.firstChild.data) / 1.0 / oldheight * newheight)
    with open(os.path.join(dir_xml, xmlfile), 'w') as fh:
        DOMTree.writexml(fh)
        print('写入name/pose OK!')

def convert():
    file_list = os.listdir(dir_pic)
    print(file_list)
    for filename in file_list:
        pic_path = dir_pic + filename
        pic_save_path = dir_pic_save + filename
        img = cv2.imread(pic_path)
        # 打印出图片尺寸
        print(img.shape)
        print(filename)
        # 将图片高和宽分别赋值给x，y
        x, y = img.shape[0:2]
        print('x = ',x ,' y = ', y) # x表示高度 y表示宽度
        modify_xml(filename)
        img_resize = cv2.resize(img, (x_size, y_size))
        cv2.imwrite(pic_save_path, img_resize)
    
if __name__ == '__main__':
    x_size = 416
    y_size = 416
    dir_pic = './test_pic/'
    dir_pic_save = './test_pic_save/'
    dir_xml = './test_xml/'
    dir_xml_save = './test_xml_save/'
    convert()

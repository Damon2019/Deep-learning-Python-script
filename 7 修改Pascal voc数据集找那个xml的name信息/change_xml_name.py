# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET

#程序功能：批量修改VOC数据集中xml标签文件的标签名称
def changelabelname(inputpath):
    listdir = os.listdir(inputpath)
    for file in listdir:
        if file.endswith('xml'):
            file = os.path.join(inputpath,file)
            tree = ET.parse(file)
            root = tree.getroot()
            for object1 in root.findall('object'):
                for sku in object1.findall('name'):           #查找需要修改的名称
                    if (sku.text == 'air'):                   #修改前的名称
                        sku.text = 'airplane'                 #修改后的名称
                        tree.write(file,encoding='utf-8')     #写进原始的xml文件并避免原始xml中文字符乱码
                    else:
                        pass
        else:
            pass

if __name__ == '__main__':
    inputpath = '/home/huangfu/xml121/xml/'
    changelabelname(inputpath)


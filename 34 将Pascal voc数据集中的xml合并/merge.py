from xml.dom.minidom import parse
import xml.dom.minidom
import os

path_xml1 = './1-xml/'
path_xml2 = './1-xml-1/'
save_path = './save/'

merge = False
for root, dirs, files in os.walk(path_xml2):
    print(files)
for data in files:
    act_data = []
    merge_data = []

    # xml1 文件
    file_xml1 = open(path_xml1 + data, 'r+')
    xml1_list = file_xml1.readlines()
    # xml2 文件
    file_xml2 = open(path_xml2 + data, 'r+')
    xml2_list = file_xml2.readlines()

    for line in xml2_list:
        if line.strip() == '<object>':
            merge = True
        elif line.strip() == '</object>':
            merge = False
            merge_data.append(line)
        if merge:
            # 插入
            merge_data.append(line)

    for line in xml1_list:
        #act_data.append(line)
        if line.strip() == '</annotation>':
            for i in merge_data:
                act_data.append(i)
        act_data.append(line)
    for i in act_data:
        p = open(save_path + data, 'a')
        p.write(i)
        p.close()

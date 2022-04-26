'''
@author: Shang Tongtong
@license: (C) Copyright 2019-present, SeetaTech, Co.,Ltd.
@contact: tongtong.shang@seetatech.com
@file: split_items_account_to_index.py
@time: 19-8-1 16:24
@desc: 根据索引把文件分开保存
'''
# -*- coding:utf-8 -*-
import os
import shutil

SUFFIX = '.jpg'

def split_and_copy(index, origdir, newdir):

    indexname = str(index) + SUFFIX
    file = os.path.join(origdir, indexname)
    shutil.copy(file, newdir)

if __name__ == '__main__':

    index_dir = r'./test.txt' #txt file
    orig_dir = r'./JPEGImages/'
    save_dir = r'./111/'

    f = open(index_dir)
    for line in f.readlines():
        linesp = line.split()[0]
        split_and_copy(linesp, orig_dir, save_dir)

# -*- coding:UTF-8 -*-
import os
import cv2
from numpy import *

# img_dir='/home/huangfu/data/coco_1/images/train2014'
img_dir='/home/huangfu/disk/1_数据集制作/第三批/voc_ship_v3/VOC2007/JPEGImages/'
img_list=os.listdir(img_dir)
# img_size=300
sum_r=0
sum_g=0
sum_b=0
count=0

for img_name in img_list:
    img_path=os.path.join(img_dir,img_name)
    img=cv2.imread(img_path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # img=cv2.resize(img,(img_size,img_size))
    sum_r=sum_r+img[:,:,0].mean()
    sum_g=sum_g+img[:,:,1].mean()
    sum_b=sum_b+img[:,:,2].mean()
    count=count+1

sum_r=sum_r/count
sum_g=sum_g/count
sum_b=sum_b/count
img_mean=[sum_r,sum_g,sum_b]
print (img_mean)

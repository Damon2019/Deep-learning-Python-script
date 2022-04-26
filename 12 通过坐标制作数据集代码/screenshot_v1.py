#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:03:02 2019
@author: Administrator

"""
import cv2
import random
import os
import os.path
import pandas as pd
import numpy  as np
from copy import deepcopy

index = 1
picNumber = 0
datPath = '/home/huangfu/桌面/dat/'
imagePath = '/home/huangfu/桌面/图片/'
saveAllImagePath = '/home/huangfu/样本/'

#-------------------------------------------------------------------------------------------
#扩大范围

#左边的线
def xl_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1 - step, slide_y1]
            l2 = [slide_x1 - step, slide_y1 + y_bSteps]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#上边的线
def yt_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1, slide_y1 - step]
            l2 = [slide_x1 + x_bSteps, slide_y1 - step]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#右边的线
def xr_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1 + x_bSteps + step, slide_y1]
            l2 = [slide_x1 + x_bSteps + step, slide_y1 + y_bSteps]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            #if D == 0:
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#下边的线
def yb_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1, slide_y1 + y_bSteps + step]
            l2 = [slide_x1 + x_bSteps, slide_y1 + y_bSteps + step]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1

#----------------------------------------------------------------------------------------
#缩小范围

#左边的线
def XR_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1 + step, slide_y1]
            l2 = [slide_x1 + step, slide_y1 + y_bSteps]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#上边的线
def YB_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1, slide_y1 + step]
            l2 = [slide_x1 + x_bSteps, slide_y1 + step]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#右边的线
def XL_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1 + x_bSteps - step, slide_y1]
            l2 = [slide_x1 + x_bSteps - step, slide_y1 + y_bSteps]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


#下边的线
def YT_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data):
    # 判断直线和矩形框是否有相交
    listD = [0]
    collectD = [-1]
    fStep = 0
    bStep = 2
    flag = 0
    for step in range(0,201,bStep):
        for k in range(len(data)):
            fStep = step
            l1 = [slide_x1, slide_y1 + y_bSteps - step]
            l2 = [slide_x1 + x_bSteps, slide_y1 + y_bSteps - step]
            sq = [data.values[k][0], data.values[k][1]+data.values[k][3], data.values[k][0]+data.values[k][2], data.values[k][1]]
            D = check(l1, l2, sq)
            listD.append(D)

        if(max(listD) == 0):
             flag = 1
             break

    if flag == 1 :
        return fStep
    else:
        return -1


# 每两个检测框框是否有交叉，如果有交集则返回重叠度 IOU, 如果没有交集则返回 0
def area_overlab(x1, y1, w1, h1, data):
    overlapRate = [0]
    for j in range(len(data)):
        x2 = data.values[j][0]
        y2 = data.values[j][1]
        w2 = data.values[j][2]
        h2 = data.values[j][3]
        if(x1>x2+w2):
            continue
        if(y1>y2+h2):
            continue
        if(x1+w1<x2):
            continue
        if(y1+h1<y2):
            continue
        colInt = abs(min(x1 +w1 ,x2+w2) - max(x1, x2))
        rowInt = abs(min(y1 + h1, y2 +h2) - max(y1, y2))
        overlap_area = colInt * rowInt
        area1 = w1 * h1
        area2 = w2 * h2
        #overlapRate 计算得出的重叠率
        if(overlap_area / area2 > 0):
            overlapRate.append(overlap_area / area2)
    return overlapRate


#根据直线求与矩形框是否相交
def check(l1,l2,sq):    #sq 代表矩形左下角和右上角的坐标
    # step 1 check if end point is in the square
    if ( l1[0] >= sq[0] and l1[1] <= sq[1] and  l1[0] <= sq[2] and  l1[1] >= sq[3]) or ( l2[0] >= sq[0] and l2[1] <= sq[1] and  l2[0] <= sq[2] and  l2[1] >= sq[3]):
        return 1
    else:
        # step 2 check if diagonal cross the segment
        p1 = [sq[0],sq[1]]
        p2 = [sq[2],sq[3]]
        p3 = [sq[2],sq[1]]
        p4 = [sq[0],sq[3]]
        if segment(l1,l2,p1,p2) or segment(l1,l2,p3,p4):
            return 1
        else:
            return 0

# 叉积判定
def cross(p1,p2,p3):
    x1=p2[0]-p1[0]
    y1=p2[1]-p1[1]
    x2=p3[0]-p1[0]
    y2=p3[1]-p1[1]
    return x1*y2-x2*y1

def segment(p1,p2,p3,p4):
    if(max(p1[0],p2[0])>=min(p3[0],p4[0])
    and max(p3[0],p4[0])>=min(p1[0],p2[0])
    and max(p1[1],p2[1])>=min(p3[1],p4[1])
    and max(p3[1],p4[1])>=min(p1[1],p2[1])):
        if(cross(p1,p2,p3)*cross(p1,p2,p4)<=0 and cross(p3,p4,p1)*cross(p3,p4,p2)<=0):
            D=1
        else:
            D=0
    else:
        D=0
    return D



'''
list = data.values[i].split();
#print(list)
cv2.waitKey (0)
cv2.destroyAllWindows()
cv2.imwrite('/home/huangfu/桌面/0511123222.tif', img)
'''


#analysisData(data)
for root, dirs, files in os.walk(imagePath):
    #print('files:', files)  # 当前路径下所有非目录子文件
    #print('tyoe files:',type(files))

    #获取文件的名称 000001
    for file in files:
        iFile = file.split(".")[0]
        #print(iFile)
        uImagePath = imagePath + iFile + '.tif'
        #print(uImagePath)
        #xml读取操作，将获取到的xml文件名送入到dom中解析
        iDatPath = datPath + iFile + '.dat'
        if not os.path.exists(iDatPath):
            print(uImagePath, '不存在对应的.dat文件')
            continue

        print('正在裁剪的图片: ', iFile + '.tif')
        img = cv2.imread(uImagePath)
        picNumber += 1
        print(img.shape)
        data = pd.read_csv(iDatPath,header=None,skiprows=[0],sep='\s+')
        for i in range(len(data)):
            if(data.values[i][0]) < 300 or data.values[i][1] < 300:
                continue
            slide_x1 = data.values[i][0] - 250
            slide_y1 = data.values[i][1] - 250
            x_bSteps = 500
            y_bSteps = 500
            overlapRate = area_overlab(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
            if max(overlapRate) == 1 and len(overlapRate) == 2:
                # cut image
                cropped = img[slide_y1 : slide_y1 + y_bSteps, slide_x1 : slide_x1 + x_bSteps]
                imgPath_1 = saveAllImagePath + str(index).zfill(6) + '.jpg'
                cv2.imwrite(imgPath_1, cropped)

            elif max(overlapRate) < 0.5 and len(overlapRate) == 2:
                # 缩小
                # 判断左边
                differ_XR = XR_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                slide_x1 += differ_XR
                x_bSteps -= differ_XR

                # 判断上边
                differ_YB = YB_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                slide_y1 += differ_YB
                y_bSteps -= differ_YB

                # 判断右边
                differ_XL = XL_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                x_bSteps -= differ_XL

                # 判断下边
                differ_YT = YT_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                y_bSteps -= differ_YT


            elif max(overlapRate) > 0.5 and len(overlapRate) == 2:
                # 放大
                # 判断左边
                differ_xl = xl_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                slide_x1 -= differ_xl
                x_bSteps += differ_xl

                # 判断上边
                differ_yt = yt_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                slide_y1 -= differ_yt
                y_bSteps += differ_yt

                # 判断右边
                differ_xr = xr_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                x_bSteps += differ_xr

                # 判断下边
                differ_yb = yb_location(slide_x1, slide_y1, x_bSteps, y_bSteps, data)
                y_bSteps += differ_yb

                '''
                if not (slide_x1 > 0 and (slide_x1 + x_bSteps) < img[1] and slide_y1 > 0 and     (slide_y1 + y_bSteps) < img[0]):
                    continue
                '''


            overlapRate_s = area_overlab(slide_x1, slide_y1, x_bSteps, y_bSteps, data)

            #if (max(overlapRate_s) == 1 and len(overlapRate_s) == 2 and slide_x1 > 0 and (slide_x1 + x_bSteps) < img[1] and slide_y1 > 0 and (slide_y1 + y_bSteps) < img[0]):
            if max(overlapRate_s) == 1 and len(overlapRate_s) == 2:


                # cut image
                dim = (600, 600)
                cropped = img[slide_y1 : slide_y1 + y_bSteps, slide_x1 : slide_x1 + x_bSteps]
                resized = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
                imgPath_1 = saveAllImagePath + str(index).zfill(6) + '.jpg'
                cv2.imwrite(imgPath_1,resized)
                index += 1



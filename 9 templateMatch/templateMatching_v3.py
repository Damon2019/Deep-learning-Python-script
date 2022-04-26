# -- coding:utf-8 --

# 1.使用SIFT或SURF计算得到模板和待匹配图像的特征点，
# 2.然后使用RANSAC或者FLANN进行特征点匹配，
# 3.最后进行仿射变换便可得到匹配的位置。

import cv2
import time
#from image_process .image_process import *
import numpy as np
from matplotlib import pyplot as plt

def filter_matches(kp1, kp2, matches, ratio = 0.5):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs

def explore_match(win, img1, img2, kp_pairs, status = None, H = None):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    # vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis = np.zeros((h2, w2), np.uint8)
    # ivis[:h1, :w1] = img1
    # vis[:h2, w1:w1+w2] = img2
    vis[:h2, :w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
    # get the position of template object find in detected image
    if H is not None:
        corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        img2 = cv2.warpPerspective(img2, H, (img2.shape[1], img2.shape[0]))
        # corners = np.int32( cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0) )
        corners = np.int32( cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) )
        print('corner = ', corners)
        cv2.polylines(image, [corners], True, (0, 0, 255)) 
    # draw lines that connect match feature points
    if status is None:
        status = np.ones(len(kp_pairs), np.bool)
    p1 = np.int32([kpp[0].pt for kpp in kp_pairs])
    p2 = np.int32([kpp[1].pt for kpp in kp_pairs]) + (w1, 0)

    green = (0, 255, 0)
    red = (0, 0, 255)
    white = (255, 255, 255)
    kp_color = (51, 103, 236)

    '''
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            col = green
            #图片上的特征点
            cv2.circle(vis, (x1, y1), 2, col, -1)
            cv2.circle(vis, (x2, y2), 2, col, -1)
        else:
            col = red
            r = 2
            # 特征点上的连线
            thickness = 3
            cv2.line(vis, (x1-r, y1-r), (x1+r, y1+r), col, thickness)
            cv2.line(vis, (x1-r, y1+r), (x1+r, y1-r), col, thickness)
            cv2.line(vis, (x2-r, y2-r), (x2+r, y2+r), col, thickness)
            cv2.line(vis, (x2-r, y2+r), (x2+r, y2-r), col, thickness)

    # 特征点上的连线
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            cv2.line(vis, (x1, y1), (x2, y2), green)
    '''

    x, y = image.shape[0:2]
    img_resize = cv2.resize(image, (int(y / 2), int(x / 2)))
    cv2.imshow(win, img_resize)
    cv2.imwrite('/home/huangfu/桌面/face/结果.jpg',img_resize)

# 程序入口
start = time.time()
img1 = cv2.imread("/home/huangfu/桌面/face/airplane.jpg")#小图模板
img2 = cv2.imread("/home/huangfu/桌面/face/泉州晋江机场.tif") #大图
image = img2.copy()

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #颜色空间转换
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img2_gray=rotate_about_center(img2_gray, 90)
#img2_gray = cv2.resize(img2_gray, (img1_gray.shape[1], img1_gray.shape[0]))

# 提取特征点
start = time.time()
#sift = surf = cv2.xfeatures2d.SURF_create()
surf = cv2.xfeatures2d.SURF_create()
# 查找关键点和描述符
kp1,des1 = surf.detectAndCompute(img1_gray, None)
kp2,des2 = surf.detectAndCompute(img2_gray, None)
end = time.time()
print ("Extract feature time:" + str(end-start))
# 一堆<KeyPoint 0x7f9880136750> 和 -7.54746562e-03
#print('kp1 = ',kp1,'des1 = ',des1)
#print('kp2 = ',kp2,'des2 = ',des2)

# 强匹配
# BFmatcher with default parms
start = time.time()
bf = cv2.BFMatcher(cv2.NORM_L2)
# 一组数据,每组分别包含三个非常重要的数据分别是queryIdx，trainIdx，distance
# 比如：[<DMatch 0x7f117af995f0>, <DMatch 0x7f117af99610>]
# 这俩个DMatch数据类型是俩个与原图像特征点最接近的俩个特征点
matches = bf.knnMatch(des1, des2, k=2)

p1, p2, kp_pairs = filter_matches(kp1, kp2, matches, ratio=0.8)
print('p1 = ', p1)
print('p2 = ', p2)
print('kp_pairs = ', kp_pairs)
end = time.time()
print ("KNN match time:" + str(end-start))

if len(p1) >= 4:
    H , status = cv2.findHomography(p1 , p2 , cv2.RANSAC , 5.0)
    print (H)
    print ('%d / %d  inliers/matched' % (np.sum(status) , len(status)))
    # do not draw outliers (there will be a lot of them)
    kp_pairs = [kpp for kpp , flag in zip(kp_pairs , status) if flag]
else:
    H , status = None , None
    print ('%d matches found, not enough for homography estimation' % len(p1))

explore_match('matches', img1_gray, img2_gray, kp_pairs, H=H)
# img3 = cv2.drawMatchesKnn(img1_gray,kp1,img2_gray,kp2,good[:10],flag=2)
end = time.time()
print ("time"+str(end-start))



cv2.waitKey(0)
cv2.destroyAllWindows()



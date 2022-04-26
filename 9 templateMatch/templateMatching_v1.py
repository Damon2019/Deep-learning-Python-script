# -*- coding: utf-8 -*-
#模板匹配
import cv2
import random
import pandas as pd
import numpy as np


index = 1

tpl = cv2.imread('/home/huangfu/桌面/web.jpg')
target = cv2.imread('/home/huangfu/桌面/people.jpeg')
print(target.shape)
cv2.namedWindow('template image', cv2.WINDOW_NORMAL)
cv2.imshow("template image", tpl)
cv2.namedWindow('target image', cv2.WINDOW_NORMAL)
cv2.imshow("target image", target)
methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]   #3种模板匹配方法
#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

th, tw = tpl.shape[:2]
for md in methods:
    print(md)
    result = cv2.matchTemplate(target, tpl, md)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if md == cv2.TM_SQDIFF_NORMED:
        tl = min_loc
    else:
        tl = max_loc
    br = (tl[0]+tw, tl[1]+th)   #br是矩形右下角的点的坐标
    cv2.rectangle(target, tl, br, (0, 0, 255), 2)
    cv2.namedWindow("match-" + np.str(md), cv2.WINDOW_NORMAL)
    cv2.imshow("match-" + np.str(md), target)
    cv2.imwrite('/home/huangfu/桌面/' + 'match-' + str(md) + '.tif', target)

cv2.waitKey(0)
cv2.destroyAllWindows()


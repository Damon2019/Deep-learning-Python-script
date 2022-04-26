# -*- coding: UTF-8 -*-
import cv2
cap=cv2.VideoCapture("/home/huangfu/objectDetection/1-深度学习代码/40 大风车裁剪视频/fengche_red_1.mp4")
# cap=cv2.VideoCapture(0) #打开设备索引号对于设备的摄像头，一般电脑的默认索引号为0
fps = 60  # 保存视频的帧率
size = (320, 256)  # 保存视频的大小
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# videoWriter = cv2.VideoWriter('video4.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
videoWriter = cv2.VideoWriter('video4111.mp4', fourcc, fps, size)
while (True):
    ret,frame=cap.read()
    if ret == True:
        # cv2.imshow("video",frame)
        frame = cv2.resize(frame, (320,256))
        videoWriter.write(frame)
    else:
        break
cap.release()
cv2.destroyAllWindows()

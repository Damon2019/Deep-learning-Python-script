import os
import cv2


imagePath = './1/'
sImagePath = './1-save/'
for root, dirs, files in os.walk(imagePath):
    for file in files:
        try:
            img = cv2.imread(imagePath+file)
            #cv2.imshow('winname', img)
            #cv2.waitKey(0)
            # cropped = img[0:128, 0:512]  # 裁剪坐标为[y0:y1, x0:x1]
            cropped = img[39:441, 357:866]  # 裁剪坐标为[y0:y1, x0:x1]

            saveImagePath = sImagePath + file

            cv2.imwrite(saveImagePath, cropped)

        except:
            print("error")

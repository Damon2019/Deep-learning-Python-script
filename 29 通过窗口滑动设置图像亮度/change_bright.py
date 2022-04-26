import os
import cv2
import numpy as np


imagePath = './pic8/'
sImagePath = './pic82/'
index = 0
for root, dirs, files in os.walk(imagePath):
    for file in files:
        img = cv2.imread(imagePath+file)
        img2 = cv2.imread(imagePath+file)

        alpha = 70
        beta = 0
        alpha = alpha * 0.01
        img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))

        saveImagePath = sImagePath + str(int(file.split('.')[0])+index).zfill(6)+'.jpg'

        cv2.imwrite(saveImagePath, img)


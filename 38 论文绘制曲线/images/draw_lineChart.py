import os
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def voc_curve(datPath):
    for root, dirs, files in os.walk(datPath):
        for file in files:
            title = file.split(".")[0]

            f=open(datPath + file)

            recall_point_all = []
            precision_point_all = []
            recall_mark_all = []
            precision_mark_all = []

            dataMat=[]
            labelMat=[]
            for line in f.readlines():
                curLine=line.strip().split(' ')
                floatLine=list(map(float,curLine))
                dataMat.append(floatLine[0:])

            step = 15
            pointStep = step
            markStep = step
            for i in range(len(dataMat)):
                # print(dataMat[i])
                if i % 2 == 0:
                    recall_point = dataMat[i][::pointStep]
                    recall_point_all.append(recall_point)
                    recall_mark = dataMat[i][::markStep]
                    recall_mark_all.append(recall_mark)
                if i % 2 == 1:
                    precision_point = dataMat[i][::pointStep]
                    precision_point_all.append(precision_point)
                    precision_mark = dataMat[i][::markStep]
                    precision_mark_all.append(precision_mark)

            plt.figure(title)
            # plt.title('---',fontsize=15)  # give plot a title
            plt.xlabel('Recall', fontsize=11)   # make axis labels
            plt.ylabel('Precision', fontsize=11)
            plt.grid(linestyle='-.')
            x = np.arange(0, 1)
            plt.plot(x,x)

            plt.plot(recall_point_all[0], precision_point_all[0], color='gold', linewidth=1.5, marker='s',ms=0.5, label='FasterRCNN*')
            plt.plot(recall_point_all[1], precision_point_all[1], color='coral', linewidth=1.5,marker='*',ms=0.8, label='MaskRCNN*')
            plt.plot(recall_point_all[2], precision_point_all[2], color='deeppink', linewidth=1.5,marker='o',ms=0.5, label='YOLOv3*')
            plt.plot(recall_point_all[3], precision_point_all[3], color='deepskyblue', linewidth=1.5,marker='^',ms=0.5, label='RFBNet*')

            plt.scatter(recall_mark_all[0], precision_mark_all[0], color='gold',marker='s',s=20)
            plt.scatter(recall_mark_all[1], precision_mark_all[1], color='coral',marker='*',s=28)
            plt.scatter(recall_mark_all[2], precision_mark_all[2], color='deeppink',marker='o',s=20)
            plt.scatter(recall_mark_all[3], precision_mark_all[3], color='deepskyblue',marker='^',s=20)


    plt.legend(markerscale=8, fontsize=11, edgecolor='gray')
    #plt.savefig("./plteps.eps", format='eps', dpi=1000, bbox_inches = 'tight')
    plt.savefig("./plteps.jpg")
    print('Created successfully!')

if __name__ == "__main__":
    datPath = 'save_coordinate/'
    voc_curve(datPath)

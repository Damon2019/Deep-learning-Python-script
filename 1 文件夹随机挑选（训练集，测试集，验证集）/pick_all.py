# author by LYS 2017/5/24
# for Deep Learning course
'''
1. read the whole files under a certain folder
2. chose 10000 files randomly
3. copy them to another folder and save
'''
import os, random, shutil

def writeTXT(folder):
    file_names = os.listdir(folder)
    for name in file_names:
        iFile = name.split(".")[0]
        fpTxt = open(folder.split('/')[0] + '.txt','a+')
        fpTxt.writelines(str(iFile).zfill(6) + '\n')
        fpTxt.close()

def copyFile(fileDir):
    pathDir = os.listdir(fileDir)
    sample = random.sample(pathDir, move_number)
    print sample
    for name in sample:
        # shutil.copyfile(fileDir+name, tarDir+name)
        shutil.move(fileDir+name, tarDir+name)
if __name__ == '__main__':
    move_number = 300
    fileDir = "train/"
    tarDir = 'val/'
    if not os.path.exists(tarDir):
        os.makedirs(tarDir)
    copyFile(fileDir)
    writeTXT(fileDir)
    writeTXT(tarDir)




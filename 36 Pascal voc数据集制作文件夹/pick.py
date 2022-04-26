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

def copyFile(fileDir, tarDir, move_number):
    pathDir = os.listdir(fileDir)
    sample = random.sample(pathDir, move_number)
    print(sample)
    for name in sample:
        # shutil.copyfile(fileDir+name, tarDir+name)
        shutil.move(fileDir+name, tarDir+name)

if __name__ == '__main__':
    move_number_val = 0
    #move_number_test = 2500
    fileDir = "train/"
    tarDir_val = 'val/'
    #tarDir_test = 'test/'
    if not os.path.exists(tarDir_val):
        os.makedirs(tarDir_val)
    #if not os.path.exists(tarDir_test):
    #    os.makedirs(tarDir_test)
    copyFile(fileDir, tarDir_val, move_number_val)
    #copyFile(fileDir, tarDir_test, move_number_test)
    writeTXT(fileDir)
    writeTXT(tarDir_val)
    #writeTXT(tarDir_test)




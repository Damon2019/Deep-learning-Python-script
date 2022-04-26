import os
import shutil
 
train_path = 'ImageSets/Main/train.txt'
xml_path = 'Annotations/'
new_path = 'train__xml/'
 
def _main():
    fp = open(train_path, 'r')
    xml_list = fp.readlines()
    fp.close()
    for file in xml_list:
        filename = file.split('\n')
        print(filename[0])
        shutil.copyfile(xml_path + filename[0]+'.xml', new_path + filename[0] +'.xml')
        #shutil.copyfile(anno_path + filename[0]+'.xml', new_anno_path + filename[0] +'.xml')
        #os.remove(anno_path + file[:9]+'.xml')
        print filename[0]+'.xml'
    print len(xml_list)
 
if __name__ == '__main__':
    _main()

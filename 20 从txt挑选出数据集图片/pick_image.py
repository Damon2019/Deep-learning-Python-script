import os
import shutil
 
train_path = 'ImageSets/Main/train.txt'
image_path = 'JPEGImages/'
new_path = 'train__image/'
 
def _main():
    fp = open(train_path, 'r')
    xml_list = fp.readlines()
    fp.close()
    for file in xml_list:
        filename = file.split('\n')
        print(filename[0])
        shutil.copyfile(image_path + filename[0]+'.jpg', new_path + filename[0] +'.jpg')
        #shutil.copyfile(anno_path + filename[0]+'.xml', new_anno_path + filename[0] +'.xml')
        #os.remove(anno_path + file[:9]+'.xml')
        print filename[0]+'.jpg'
    print len(xml_list)
 
if __name__ == '__main__':
    _main()

import os
import shutil
 
train_path = '2007_val.txt'
txt_path = 'labels1/'
new_path = 'labels/val2007/'
 
def _main():
    fp = open(train_path, 'r')
    xml_list = fp.readlines()
    fp.close()
    for file in xml_list:
        # filename = file.split('\n')
        filename = file.split('/')[3].split('.')[0]
        # print(filename)
        shutil.copyfile(txt_path + filename +'.txt', new_path + filename +'.txt')
        #shutil.copyfile(anno_path + filename[0]+'.xml', new_anno_path + filename[0] +'.xml')
        #os.remove(anno_path + file[:9]+'.xml')
        print(filename+'.txt')
    print len(xml_list)
 
if __name__ == '__main__':
    _main()

import os  
import shutil 
 
print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
path = input('请键入需要整理的文件夹地址：')
new_path = input('请键入要复制到的文件夹地址：')
 
for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        #print(files[i])
        if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png') or (files[i][-3:] == 'JPG'):
            file_path = root+'/'+files[i]  
            new_file_path = new_path+ '/'+ files[i]  
            shutil.copy(file_path,new_file_path)  
 
#yn_close = input('是否退出？')

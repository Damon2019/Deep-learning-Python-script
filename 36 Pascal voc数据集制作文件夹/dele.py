import os
 
#批量重命名文件
dir = r'./test_xml'
list = os.listdir(dir)
os.chdir(dir)
for file in list :
    new = file.split("final")[1]
    print(new)
    os.rename('F:\objectDetection\\1-深度学习代码\\0数据集制作文件夹\\test_xml\\' + file,'F:\objectDetection\\1-深度学习代码\\0数据集制作文件夹\\test_xml_save\\' + new)

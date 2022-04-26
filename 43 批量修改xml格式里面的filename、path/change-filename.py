import os
import os.path
import xml.dom.minidom
path="./Annotations"
files=os.listdir(path)#返回文件夹中的文件名列表
#print(files)
s=[]
count=0
for xmlFile in files:
    if not os.path.isdir(xmlFile):#os.path.isdir()用于判断对象是否为一个目录
        try:
            #如果不是目录，则直接打开
            name1=xmlFile.split('.')[0]
            print(name1)
            dom=xml.dom.minidom.parse(path+'\\'+xmlFile)
            #print(dom)
            root=dom.documentElement
            newfolder=root.getElementsByTagName('folder')
            newpath = root.getElementsByTagName('path')
            newfilename = root.getElementsByTagName('filename')

            if newfolder == []:
                pass
            else:
                newfolder[0].firstChild.data = 'car.jpg'

            if newpath == []:
                pass
            else:
                newpath[0].firstChild.data = 'car.jpg'

            if newfilename == []:
                pass
            else:
                newfilename[0].firstChild.data = 'car.jpg'
            #print(newfolder)
            print('path = ', newpath)
            print('type path = ', type(newpath))

            #newfilename[0].firstChild.data = 'car.jpg'
            #newfolder[0].firstChild.data = 'car.jpg'
            #newpath[0].firstChild.data = 'car.jpg'
            with open(os.path.join(path, xmlFile), 'w') as fh:
                dom.writexml(fh)
                #print('写入name/pose OK!')
            count = count + 1
        except:
            print('pass')

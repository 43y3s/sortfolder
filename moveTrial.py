import shutil
import glob
import os

fullpath = os.path.join
fileExt = os.path.splitext

src = r"C:\enterdirectory"
mydict = {}

files = os.listdir(src)

typeList = set([])
newFolder = set([])
nameList = set([])

for file in files:
    fileType = fileExt(file)[1]
    fileName = fileExt(file)
    
    if fileType not in typeList and fileName not in nameList:
        typeList.add(fileType)
        nameList.add(fileName)
        name = (fileType[1:] + "files")
        try:
            print('Making directories: ' + name)
            os.mkdir(fullpath(src, name))
        except:
            print('Error')
        mydict.update({fullpath(src,name): fileType})
        
for destination, extension in mydict.items():
    for file in files:
        if fileExt(file)[1] == extension:
            try:
                print (fullpath(src, file) + " -> " + destination) 
                shutil.move(fullpath(src,file), destination)
            except:
                pass


import os
global FileList
FileList = []
for (root,dirs,files) in os.walk("E:\\01331 (Title-Artist) (8-GB)"):
    FileList = FileList + files
print(sorted(FileList))

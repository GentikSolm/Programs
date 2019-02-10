import os
for folderName, subfolders, filenames in os.walk("E:\\01331 (Title-Artist) (8-GB)"):
    #print(folderName+"\\"+subfolders+"\\"+filenames)
    for file in filenames:
        print(folderName+"\\"+file)

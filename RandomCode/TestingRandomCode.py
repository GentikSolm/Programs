import os

for folderName, subfolders, filenames in os.walk("E:\\TEST1331"):
    for file in filenames:
        if ".cdg" in file.lower() or ".mp3" in file.lower():
            #sortedSongList.append(folderName+"\\"+file)
            print("-- "+file)
        elif ".cdg" or ".mp3" not in file.lower():
            #ExtraFiles.append(folderName+"\\"+file)
            print("!! "+file)

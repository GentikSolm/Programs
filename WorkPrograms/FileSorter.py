import string
import os
import tempfile
import shutil
import sys
def WhereFilePath():
    global FilePathInput
    #FilePath = input("Where is the file you would like to sort?\n-> ")
    FilePathInput = "E:\\TEST1331"
# Book maker must be seperable from file sorter! Also, File FileSorter
#    Must have option to Not create sub folders
#FileList = list(string.ascii_lowercase)
def GetUpperFilePath(PathInput):
    global upperFilePath
    ListupperFilePath = PathInput.split("\\")
    if ListupperFilePath[0] == ListupperFilePath[-2]:
        return ListupperFilePath[-2]+"\\"
    else:
        return ListupperFilePath[-2]

def FileSorter(FilePath,ReqSub):

    """
    SOLVED

    Create array of file paths that need to be moved, then move that array to specefied folder inside origin, then sort.
    also, Create folder in same area as specefied folder, then create its sub folders as needed as transfer of songs start.

    """
    global sortedSongList
    sortedSongList = []
    os.mkdir(GetUpperFilePath(FilePathInput))
    countForBreak = 0
    for folderName, subfolders, filenames in os.walk(FilePath):
        countForBreak += 1
        if countForBreak == 2:
            print("Success!")
            break
        print("Loading songs into TempList")
        loadBar(filenames)
        count = 0
        for file in filenames:
            #Moving Progress bar
            count += percent
            if count >= 1:
                count = 0
                moveBar()
            #Adding files to sortedSongList
            if ".cdg" or ".mp3" in file:
                sortedSongList.append(folderName+"\\"+file,tmpfolder)
    if ReqSub == True:
        moveToFOlders(ReqSub)
    elif ReqSub == False:
        moveToFOlders(ReqSub)
    else:
        print("Invalid input, Defaulting to no sub folders.")
    sortedSongList.sort()
    print("\nDone!")

def moveToFOlders(reqSub):
    pass

def loadBar(size):
    global length
    length = 30
    global percent
    percent = length/len(size)
    #print("Writing to file")
    sys.stdout.write("[{0}]".format(" " * (length)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (length))
def moveBar():
    sys.stdout.write('\b=>')
    sys.stdout.flush()

WhereFilePath()
FileSorter(FilePathInput,True)

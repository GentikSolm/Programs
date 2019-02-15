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

def parseInputs(Path, subFiles):
    #Make sure all inputs are good. Dont want to move the wrong folder / things
    pass



def GetUpperFilePath(PathInput):
    global ListupperFilePath
    ListupperFilePath = PathInput.split("\\")
    # if ListupperFilePath[0] == ListupperFilePath[-2]:
    #     return ListupperFilePath[-2]+"\\"
    # else:
    return ListupperFilePath[-2]

def FileSorter(FilePath,ReqSub):
    sortedSongList = []
    try:
        os.mkdir(GetUpperFilePath(FilePathInput) + "\\New" + ListupperFilePath[-1])
    except FileExistsError:
        print("\nERROR\nFolder already exists!\n")
        pass

    countForBreak = 0
    for folderName, subfolders, filenames in os.walk(FilePath):
        countForBreak += 1
        if countForBreak == 2:
            print("\nSuccess!")
            break
        print("Loading songs into List")
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
                sortedSongList.append(folderName+"\\"+file)
    moveToFolders(sortedSongList, ReqSub)
    #sortedSongList.sort()
    print("\nDone!")

def moveToFolders(myList, subFoldersNeeded):
    myList.sort()
    sys.stdout.write("Writing ")
    if subFoldersNeeded == True:
        pass
    elif subFoldersNeeded == False:
        pass
    else:
        print("Im sorry, i dont understand!")
        pass

    for i in myList:
        #print(a)
        sys.stdout.write(i)
        sys.stdout.flush()
        # NEEDS TO BE FIXED
        sys.stdout.write("\b" * len(i))
        sys.stdout.flush()
        #print(i)

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

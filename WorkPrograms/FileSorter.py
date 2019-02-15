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
    global OrigionalFolderName
    OrigionalFolderName = ListupperFilePath.pop()
    global UpperFilePath
    UpperFilePath = ListupperFilePath[0]
    for i in ListupperFilePath[1:]:
        UpperFilePath +="\\"+i

    # if ListupperFilePath[0] == ListupperFilePath[-2]:
    #     return ListupperFilePath[-2]+"\\"
    # else:
    return UpperFilePath + "\\New" + OrigionalFolderName

def FileSorter(FilePath,ReqSub):
    sortedSongList = []
    ExtraFiles = []
    try:
        os.mkdir(GetUpperFilePath(FilePath))
    except FileExistsError:
        print("\nERROR\nFolder already exists!\n")
        return
    print("Loading songs into List")
    #countForBreak = 0
    for folderName, subfolders, filenames in os.walk(FilePath):
        sys.stdout.write("\n")
        percentCount = loadBar(filenames)
        count = 0
        for file in filenames:
            #Moving Progress bar
            count += percentCount
            if count >= 1:
                count = 0
                moveBar()
            #Adding files to sortedSongList
            if ".cdg" or ".mp3" in file.lower():
                sortedSongList.append(folderName+"\\"+file)
            elif ".cdg" or ".mp3" not in file.lower():
                ExtraFiles.append(folderName+"\\"+file)
    moveToFolders(sortedSongList, ReqSub, FilePath)
    print("\nDone!")

def moveToFolders(myList, subFoldersNeeded,FilePath):
    myList.sort()
    sys.stdout.write("\nWriting ")

    if subFoldersNeeded == True:

        pass
    elif subFoldersNeeded == False:
        for i in myList:
            loadSongName(i)
            shutil.move(i, GetUpperFilePath(FilePath))


    else:
        print("Im sorry, i dont understand!")
        pass
def loadSongName(name):
    sys.stdout.write(name)
    sys.stdout.flush()
    # NEEDS TO BE FIXED
    sys.stdout.write("\b" * len(name))
    sys.stdout.flush()

def loadBar(size):
    if len(size) == 0:
        return
    global length
    length = 30
    percent = length/len(size)
    #print("Writing to file")
    sys.stdout.write("[{0}]".format(" " * (length)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (length))
    return percent
def moveBar():
    sys.stdout.write('\b=>')
    sys.stdout.flush()



WhereFilePath()
FileSorter(FilePathInput,False)

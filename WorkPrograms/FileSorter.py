import string, os, shutil, sys

def WhereFilePath():
    global FilePathInput
    #FilePath = input("Where is the file you would like to sort?\n-> ")
    FilePathInput = "E:\\TEST1331"
# Book maker must be seperable from file sorter! Also, File FileSorter
#    Must have option to Not create sub folders
#FileList = list(string.ascii_lowercase)
#1000 per folder

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
            count += 1
            if percentCount != "small" and count >= percentCount:
                count = 0
                moveBar()
            #Adding files to sortedSongList
            if ".cdg" in file.lower() or ".mp3" in file.lower():
                sortedSongList.append(folderName+"\\"+file)
            elif ".cdg" not in file.lower() or ".mp3" not in file.lower():
                ExtraFiles.append(folderName+"\\"+file)
    moveToFolders(sortedSongList, ReqSub, FilePath, ExtraFiles)
    print("\nDone!")


def moveToFolders(myList, subFoldersNeeded,FilePath, anyExtraFiles):
    myList.sort()
#NEED TO FINISH THESE STATEMENTS!!!!!!!!!!!!!! FILE SORTING
    if subFoldersNeeded == True:
        letter = None
        maxFolderSize = 1000
        currentSize = 0
        currentnum = 0
        currentFolder = GetUpperFilePath(FilePath) + "\\" + Letter
        lastfile = myList[0]
        for file in myList:
            if file[0].upper() == lastfile[0].upper():
                currentSize += 1
                if currentSize >= maxFolderSize:
                    currentnum += 1
                    currentSize = 0
                if currentnum != 0:
                    pass
                else:
                    pass
                Letter = file[0].upper()
                lastfile = file

                #while currentSize <= maxFolderSize:

    elif subFoldersNeeded == False:
        sys.stdout.write("\nWriting ")
        for i in myList:
            loadFileName(i)
            shutil.move(i, GetUpperFilePath(FilePath))
        if len(anyExtraFiles) != 0:
            sys.stdout.write("\nWriting ")
            os.mkdir(GetUpperFilePath(FilePath) + "\\EXTRAFILES")
            for j in anyExtraFiles:
                loadFileName(j)
                shutil.move(j, GetUpperFilePath(FilePath) + "\\EXTRAFILES")
            sys.stdout.write("\nEXTRA FILES FOUND, PLEASE REMOVE FROM NEW FOLDER")
    else:
        print("Im sorry, i dont understand!")
        pass


#Functions for Progress bar, not intended for final use.
def loadFileName(name):
    sys.stdout.write(name)
    sys.stdout.flush()
    # NEEDS TO BE FIXED
    sys.stdout.write("\b" * len(name))
    sys.stdout.flush()
def loadBar(size):
    global length
    length = 30
    if len(size) <= length:
        return "small"
    percent = len(size)/length
    #print("Writing to file")
    sys.stdout.write("[{0}]".format(" " * (length)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (length))
    return percent
def moveBar():
    sys.stdout.write('\b=>')
    sys.stdout.flush()
#End Progress bar functions ------------------------------


WhereFilePath()
FileSorter(FilePathInput,False)

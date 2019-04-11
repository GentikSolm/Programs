import string, os, shutil, sys

def WhereFilePath():
    global FilePathInput
    #FilePath = input("Where is the file you would like to sort?\n-> ")
    FilePathInput = "D:\\Testing\\01331 (Title-Artist) (8-GB) Origional"
# Book maker must be seperable from file sorter! Also, File FileSorter
#    Must have option to Not create sub folders
#FileList = list(string.ascii_lowercase)
#1000 per folder
def parseInputs(Path, subFiles):
    #Make sure all inputs are good. Dont want to move the wrong folder / things
    pass
def GetUpperFilePath(PathInput):
    ListupperFilePath = PathInput.split("\\")
    OrigionalFolderName = ListupperFilePath.pop()
    #UpperFilePath = ListupperFilePath[-1]
    UpperFilePath = ListupperFilePath[0]
    for i in ListupperFilePath[1:]:
        UpperFilePath +="\\"+i
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
    for (folderName, subfolders, filenames) in os.walk(FilePath):
        sys.stdout.write("\n")
        percentCount = loadBar(filenames)
        count = 0
        subfolders.sort()
        tmp = []
        for file in filenames:
            #Moving Progress bar
            count += 1
            if percentCount != "small" and count >= percentCount:
                count = 0
                moveBar()
            #Adding files to sortedSongList
            if ".cdg" in file.lower() or ".mp3" in file.lower():
                sortedSongList.append(os.path.join(folderName, file))
            else:
                ExtraFiles.append(folderName+"\\"+file)
    copyToFolders(sortedSongList, ReqSub, FilePath, ExtraFiles)

    print("\nDone!")
def copyToFolders(myList, subFoldersNeeded, FilePath, anyExtraFiles):
    myList.sort(key=str.lower)
    if subFoldersNeeded == True:
        maxFolderSize = 1000
        currentSize = 0
        currentnum = 0
        currentFolder = GetUpperFilePath(FilePath)
        lastfile = myList[0]
        percentCount = loadBar(myList)
        count = 0
        for filewp in myList:
            file = filewp.split("\\")[-1]
            currentSize += 1
            #Places file in folder with same letter if letter is the same as previous file
            if file[0].upper() == lastfile[0].upper() and file[0].lower() in list(string.ascii_lowercase) or file[0].upper() == lastfile[0].upper() and file[0] in list("123456789"):
                Letter = file[0].upper()
                if currentSize >= maxFolderSize:
                    currentnum += 1
                    currentSize = 0
                if currentnum != 0:
                    Letter = Letter[0] + " - " + str(currentnum)
                currentSize +=1
                    #Handles files that do not start with a Letter
                #Changes letter and resets counter
            elif file[0].upper() != lastfile[0].upper():
                currentSize = 0
                currentnum = 0
                Letter = file[0].upper()
                #while currentSize <= maxFolderSize:
            else:
                Letter = "0"
                if currentSize >= maxFolderSize:
                    currentnum += 1
                    currentSize = 0
                if currentnum != 0:
                    Letter = Letter[0] + " - " + str(currentnum)
                    currentSize += 1
            newfolder = currentFolder + "\\" + Letter
            try:
                os.mkdir(newfolder)
            except:
                pass
            shutil.copy(filewp,newfolder)
            lastfile = file
            count += 1
            if percentCount != "small" and count >= percentCount:
                count = 0
                moveBar()

    elif subFoldersNeeded == False:
        sys.stdout.write("\nWriting ")
        for i in myList:
            loadFileName(i)
            shutil.copy(i, GetUpperFilePath(FilePath))
        if len(anyExtraFiles) != 0:
            sys.stdout.write("\nWriting ")
            os.mkdir(GetUpperFilePath(FilePath) + "\\EXTRAFILES")
            for j in anyExtraFiles:
                loadFileName(j)
                shutil.copy(j, GetUpperFilePath(FilePath) + "\\EXTRAFILES")
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
FileSorter(FilePathInput,True)

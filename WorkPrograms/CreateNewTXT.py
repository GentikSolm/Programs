import os, sys, string
global ListOfGoodStrings
ListOfGoodStrings = "0123456789()"
global SongNumber
SongNumber = 100000
def AskFileInfo():
    """
    This function Grabs all data that will be used in list generation, such as root folder location, song number, and file name.
    """
    #Grabs Filename
    global FileName
    FileName = input("What do you want the txt files name to be?\n-> ")
    #Grabs File Path
    global FilePath
    FilePath = input("Where is the Song Folder Located? (Copy paste from File Explorer, then right click on console)\n-> ")
    #Grabs desired file type
    global FileKind
    FileKind = input("What kind of file do you want to make?\n0 -> MP3 songlist\n1 -> 787 txt file\n-> ")
    return
#Function for MP3 Song Book

#SORTS TO Z FOLDER
def createMp3txtFile(InPath):
    global FileList
    FileList = []
    for (root,dirs,files) in os.walk(InPath):
        dirs.sort()
        tempFileList = []
        for file in files:
            while file[0].lower() not in list(string.ascii_lowercase) and file[0] not in list(ListOfGoodStrings):
                file = file[1:]
            tempFileList.append(file)
        tempFileList.sort(key=str.lower)
        FileList.extend(tempFileList)

    NewSongFile = open(FileName+'.txt', mode='w')
    #Song number counter
    global i
    i = 0
    #For loop generation of mp3 file list
    loadBar(FileList)
    count = 0
    for entry in FileList:
        count += percent
        if count >= 1:
            count = 0
            moveBar()
        if 'mp3' in entry:
            i +=1
            num = 100000 + i
            Snum = str(num)[1:]
            Fname = entry[:-4].replace(" - ","|")
            NewSongFile.write(f'{Snum}|{Fname}\n')
    NewSongFile.close()
    print("")
    return
#Function for 787 txt file
def create787TxtDoc(InPath):
    #Counter for File location in folder
    i = 0
    """
    FileList is the parent list of all the file names in every folder. os.walk() seperates all files in each folder into their own list,
    therefore when plugged into the for loop, get combined into a master list to be sorted and used later in function
    """
    #Creating FileList
    global FileList
    FileList = []
    global badlist
    badlist = []
    #Finding all files, and making Master list
    #place 0 is file name, 1 is file path, 2 is file extension
    for (root,dirs,files) in os.walk(InPath):
        for file in files:
            while file[0].lower() not in list(string.ascii_lowercase) and file[0] not in list(ListOfGoodStrings):
                file = file[1:]
            if file[0].lower() in list(string.ascii_lowercase) or file[0] in list(ListOfGoodStrings):
                FileList.append([file[:-4], os.path.join(root, file), file[-4:]])
            else:
                badlist.append(os.path.join(root, file))
    #Opening txt file and writing info to it
    NewSongFile = open(FileName + '.txt', mode='w')
    #This is the header in the text document
    NewSongFile.write("Songnum	Nation	Songtype	Language	Title	Singer\n")
    #This starts the recusion through the list, in order, creating each line of the text doc.
    loadBar(FileList)
    count = 0
    for Sentry in FileList.sort():
        count += percent
        if count >= 1:
            count = 0
            moveBar()
        nation = "2"
        songType = "8"
        language = "2"
        if ".mp3" == Sentry[2].lower():
            i += 1
            splitSentry = Sentry[0].split(" - ")
            title = splitSentry[0]
            artist = splitSentry[1]
            CDGFile = Sentry[1][:-4] +".cdg"
            MP3File = Sentry[1]
            #This is the main part of the txt string generation. I formatted it so that it is easier to manipulate :)
            NewSongFile.write(f"#{str(SongNumber + i)[1:]}\t#{nation}\t#{songType}\t#{language}\t#{title}\t#{artist}\t#{MP3File}\t#{CDGFile}\n")
        elif ".cdg" == Sentry[2].lower():
            pass
        else:
            print(f"EXTRA FILES FOUND\nTYPE: {Sentry[2]}\nNAME: {Sentry[0]}\nLOCATION: {Sentry[1]}")
    #Closing the text doc
    NewSongFile.close()
    if len(badlist) != 0:
        print("FOUND BAD ENTRIES:")
        for i in badlist:
            print(i)
    else:
        print("\nDone!")
    return
def callwhichfun(FileKindNum):
    if FileKindNum == "0":
        createMp3txtFile(FilePath)
        return False
    elif FileKindNum == "1":
        create787TxtDoc(FilePath)
        return False
    else:
        print('I dont understand! Please input 0 or 1!')
        FileKind = input("-> ")
        return True
    return
def loadBar(size):
    global length
    length = 30
    global percent
    percent = length/len(size)
    print("Writing to file")
    sys.stdout.flush()
    sys.stdout.write("[{0}]".format(" " * (length)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (length))
    sys.stdout.flush()
def moveBar():
    sys.stdout.write('\b->')
    sys.stdout.flush()
#Calling all functions.
AskFileInfo()
while callwhichfun(FileKind) == True:
     callwhichfun(FileKind)

#callwhichfun(FileKind)
exit = input("Press enter to exit")

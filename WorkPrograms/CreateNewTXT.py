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
        for file in files:
            if file[0].lower() not in list(string.ascii_lowercase) and file[0] not in list(ListOfGoodStrings):
                file = file[1:]
                FileList.append(file)
            elif file == "":
                pass
            else:
                FileList.append(file)
    NewSongFile = open(FileName+'.txt', mode='w')
    #Song number counter
    global i
    i = 0
    #For loop generation of mp3 file list
    loadBar(FileList)
    count = 0
    for entry in sorted(FileList):
        count += percent
        if count >= 1:
            count = 0
            moveBar()
        if 'mp3' in entry:
            i +=1
            num = 100000 + i
            Snum = str(num)[1:]
            Fname = entry[:-4].replace(" - ","|")
            NewSongFile.write('{0}|{1}\n'.format(Snum, Fname))
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
    #Finding all files, and making Master list
    #place 0 is file name, 1 is file path, 2 is file extension
    for (root,dirs,files) in os.walk(InPath):
        for file in files:
            if file[0].lower() not in list(string.ascii_lowercase) and file[0] not in list(ListOfGoodStrings):
                Modfile = file[1:]
                if Modfile[0] == " ":
                    Modfile = Modfile[1:]
                FileList.append([Modfile[:-4], os.path.join(root, file), file[-4:]])
            elif file == "":
                pass
            else:
                FileList.append([file[:-4], os.path.join(root, file), file[-4:]])
    #Opening txt file and writing info to it
    NewSongFile = open(FileName + '.txt', mode='w')
    #This is the header in the text document
    NewSongFile.write("Songnum	Nation	Songtype	Language	Title	Singer\n")
    #This starts the recusion through the list, in order, creating each line of the text doc.
    loadBar(FileList)
    count = 0
    nation = "2"
    songType = "8"
    language = "2"
    for Sentry in sorted(FileList):
        count += percent
        if count >= 1:
            count = 0
            moveBar()
        if ".mp3" == Sentry[2].lower():
            i += 1
            splitSentry = Sentry[0].split(" - ")
            title = splitSentry[0]
            artist = splitSentry[1]
            CDGFile = Sentry[1][:-4] +".cdg"
            MP3File = Sentry[1]
            #This is the main part of the txt string generation. I formatted it so that it is easier to manipulate :)
            NewSongFile.write("#{0}\t#{1}\t#{2}\t#{3}\t#{4}\t#{5}\t#{6}\t#{7}\n".format(str(SongNumber + i)[1:], nation, songType, language, title, artist, MP3File, CDGFile))
        elif ".cdg" == Sentry[2].lower():
            pass
        else:
            print("EXTRA FILES FOUND\nTYPE: {0}\nNAME: {1}\nLOCATION: {2}".format(Sentry[2]), Sentry[0], Sentry[1])
            pass
    #Closing the text doc
    NewSongFile.close()
    print("")
    return
def callwhichfun(FileKindNum):
    if FileKindNum == "0":
        createMp3txtFile(FilePath)
        #replaceChar()
    elif FileKindNum == "1":
        create787TxtDoc(FilePath)
        #replaceChar()
    else:
        print('I dont understand! Please input 0 or 1!')
    return
def loadBar(size):
    global length
    length = 30
    global percent
    percent = length/len(size)
    print("Writing to file")
    sys.stdout.write("[{0}]".format(" " * (length)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (length))
def moveBar():
    sys.stdout.write('\b->')
    sys.stdout.flush()
#Calling all functions.
AskFileInfo()
#rename files for bad characters
callwhichfun(FileKind)
print("Done!")
exit = input("Press enter to exit")

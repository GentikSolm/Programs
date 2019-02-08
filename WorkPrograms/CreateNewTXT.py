import os

def AskFileInfo():

    """
    This function Grabs all data that will be used in list generation, such as root folder location, song number, and file name.
    Song number is turned off because im not sure if that actually ever changes. Feel free to enable
    """
    #Grabs Filename
    global FileName
    FileName = input("File Name?\n-> ")
    #Grabs Song Number
    global SongNumber
    SongNumber = ""
    #SongNumber = input("Starting Song Number? (Press Enter for default)\n-> ")
    if SongNumber == "":
        SongNumber = 10000
    else:
        SongNumber = int(SongNumber)
    #Grabs File Path
    global FilePath
    FilePath = input("Where is the Song Folder Located? (Copy paste from File Explorer)\n-> ")
    global FileKind
    FileKind = input("What kind of file do you want to make?\n0 -> MP3 songlist\n1 -> 787 txt file\n-> ")
    return


def createMp3txtFile(InPath):
    global FileList
    FileList = []
    for (root,dirs,files) in os.walk(InPath):
        FileList = FileList + files
    NewSongFile = open(FileName+'.txt', mode='w')
    global i
    i = 0
    for entry in sorted(FileList):
        if 'mp3' in entry:
            i +=1
            num = 100000 + i
            Snum = str(num)[1:]
            Fname = entry[:-4]
            NewSongFile.write('{0}:{1}\n'.format(Snum, Fname))
    NewSongFile.close()
    return

def create787TxtDoc(InPath):
    #Counter for File location in folder
    i = 0
    """
    Filelist is the parent list of all the file names in every folder. os.walk() seperates all files in each folder into their own list,
    therefore when plugged into the for loop, get combined into a master list to be sorted and used later in function
    """
    #Creating Filelist
    global Filelist
    Filelist = []
    #Finding all files, and making Master list
    for (root,dirs,files) in os.walk(InPath):
        Filelist = Filelist + files
    #Opening txt file and writing info to it
    NewSongFile = open(FileName + '.txt', mode='w')
    #This is the header in the text document
    NewSongFile.write("Songnum	Nation	Songtype	Language	Title	Singer\n")
    #This starts the recusion through the list, in order, creating each line of the text doc.
    for entry in sorted(Filelist):
        nation = "2"
        songType = "8"
        language = "2"
        Sentry = entry
        #I had to reverse cdg and mp3, if you look, this if statement is actually placing the mp3 file location and not cdg, the other if loop is
        #reversed the same way.
        if ".cdg" in Sentry:
            i += 1
            splitSentry = Sentry.split(" - ")
            title = splitSentry[0]
            artist = splitSentry[1][:-4]
            MP3File = Sentry[:-4]+".mp3"
            #This is the main part of the txt string generation. I formatted it so that it is easier to manipulate :)
            NewSongFile.write("#{0}\t#{1}\t#{2}\t#{3}\t#{4}\t#{5}\t#N:\\Custom HD787\\{6}\t".format(str(SongNumber + i), nation, songType, language, title, artist, MP3File ))
        #This attaches the cdg file to the end of the previous line, and starts a new line.
        elif ".mp3" in Sentry:
            CDGFile = Sentry[:-4]+".cdg"
            NewSongFile.write("#N:\\Custom HD787\\{0}\n".format(CDGFile))
        else:
            pass
    #Closing the text doc
    NewSongFile.close()
    return

def replaceBackslash():
    #This, im not actually sure if its required, more less to be safe.
    #Also, if you want to replace anything in the text doc, here is the place to do it.
    global TextString
    Textfile = open(FileName + '.txt', mode='r')
    TextString = Textfile.read()
    #If you want to replace anything else, here is where it would go.
    #TextString = TextString.replace("><","\\")
    Textfile.close()
    Textfile = open(FileName + '.txt', mode='w')
    Textfile.write(TextString)
    Textfile.close()
    return
def callwhichfun(FileKindNum):
    if FileKindNum == "0":
        createMp3txtFile(FilePath)
        #replaceBackslash()
    elif FileKindNum == "1":
        create787TxtDoc(FilePath)
        replaceBackslash()
    else:
        print('I dont understand! Please input 0 or 1!')
AskFileInfo()
callwhichfun(FileKind)
#Calling all functions.
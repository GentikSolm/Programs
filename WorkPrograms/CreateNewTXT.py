import os
import sys

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
#Function for MP3 Song Book
def createMp3txtFile(InPath):
    #Mostly same as what is in 787 code, see line
    global FileList
    FileList = []
    for (root,dirs,files) in os.walk(InPath):
        FileList = FileList + files
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
    for (root,dirs,files) in os.walk(InPath):
        FileList = FileList + files
    #Opening txt file and writing info to it
    NewSongFile = open(FileName + '.txt', mode='w')
    #This is the header in the text document
    NewSongFile.write("Songnum	Nation	Songtype	Language	Title	Singer\n")
    #This starts the recusion through the list, in order, creating each line of the text doc.
    loadBar(FileList)
    count = 0
    for entry in sorted(FileList):
        count += percent
        if count >= 1:
            count = 0
            moveBar()
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
            NewSongFile.write("#{0}\t#{1}\t#{2}\t#{3}\t#{4}\t#{5}\t#N:\\Custom HD787\\{6}\t".format(str(SongNumber + i)[1:], nation, songType, language, title, artist, MP3File ))
        #This attaches the cdg file to the end of the previous line, and starts a new line.
        elif ".mp3" in Sentry:
            CDGFile = Sentry[:-4]+".cdg"
            NewSongFile.write("#N:\\Custom HD787\\{0}\n".format(CDGFile))
        else:
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
def FileSorter():
    pass
def PDFCreator():
    pass



#Calling all functions.

AskFileInfo()
#rename files for bad characters
callwhichfun(FileKind)
print("Done!")

import os

def AskFileInfo():
    global FileName
    FileName = input("File Name?\n-> ")
    global SongNumber
    SongNumber = input("Starting Song Number? (Press Enter for default)\n-> ")
    if SongNumber == "":
        SongNumber = 10000
    else:
        SongNumber = int(SongNumber)
    global FilePath
    FilePath = input("Where is the Song Folder Located? (Copy paste from File Explorer)\n-> ")
    return
AskFileInfo()
#Counter for File location in folder
def createTxtDoc(InPath):
    i = 0
    #with os.listdir(InPath) as ListOfEntries:
    ListOfEntries = os.listdir(InPath)
    ListOfEntries.sort()
    NewSongFile = open(FileName + '.txt', mode='w')
    NewSongFile.write("Songnum	Nation	Songtype	Language	Title	Singer\n")
    for entry in ListOfEntries:
        nation = "2"
        songType = "8"
        language = "2"
        #ListOfEntries.sort()
        #for entry in ListOfEntries:
        #Sentry = str(entry)[11:-2]
        #Sentry = entry.name
        Sentry = entry
        if ".cdg" in Sentry:
            i += 1
            splitSentry = Sentry.split(" - ")
            title = splitSentry[0]#[:-4]
            artist = splitSentry[1][:-4]
            MP3File = Sentry[:-4]+".mp3"
            NewSongFile.write("#{0}\t#{1}\t#{2}\t#{3}\t#{4}\t#{5}\t#N:><Custom HD787><{6}\t".format(str(SongNumber + i), nation, songType, language, title, artist, MP3File ))

        elif ".mp3" in Sentry:
            CDGFile = Sentry[:-4]+".cdg"
            NewSongFile.write("#N:><Custom HD787><{0}\n".format(CDGFile))
        else:
            pass
    NewSongFile.close()
        #FN = File Number, or the Place value of the file in the folder list view
        #FileLoc = File Location
        #FIND AND REPLACE ALL >< WITH \
    return
def replaceBackslash():
    global TextString
    Textfile = open(FileName + '.txt', mode='r')
    TextString = Textfile.read()
    TextString = TextString.replace("><","\\")
    Textfile.close()
    Textfile = open(FileName + '.txt', mode='w')
    Textfile.write(TextString)
    Textfile.close()
    return
createTxtDoc(FilePath)
replaceBackslash()

#POETSD = Post Element Tree Song Data

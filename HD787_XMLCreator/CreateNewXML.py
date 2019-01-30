import xml.etree.ElementTree as ET
import os

EncodeData = """<?xml version="1.0"?>"""

def AskFileInfo():
    global FileName
    FileName = input("File Name?\n-> ")
    global SongNumber
    SongNumber = input("Starting Song Number? (Press Enter for default)\n-> ")
    if SongNumber == "":
        SongNumber = 10000
    else:
        pass
    global FilePath
    FilePath = input("Where is the Song Folder Located? (Copy paste from File Explorer)\n-> ")
    return
AskFileInfo()
#Counter for File location in folder
def createXmlData(InPath):
    i = 0
    #Create Parent XML element
    global data
    data = ET.Element('data')
    with os.scandir(InPath) as ListOfEntries:
        for entry in ListOfEntries:
            Sentry = str(entry)
            if ".cdg" in Sentry:
                i += 1
                ItemNum = "Item" + str(i)
                ItemNum = ET.SubElement(data, ItemNum)
                ItemNum.set('SongNum', "#" + str(SongNumber) + str(i))
                ItemNum.set('NationCode', '#2')
                ItemNum.set('SongType', '#8')
                ItemNum.set('Language', '#2')
                #ItemNum.set('Title', '#' + Title)
                #ItemNum.set('Singer', "#" + Singer)
                ItemNum.set('CDGLoc', "#" + InPath + "\\" + Sentry)
            elif ".mp3" in Sentry:
                ItemNum.set('MP3Loc', "#" + InPath + "\\" + Sentry)
        #FN = File Number, or the Place value of the file in the folder list view
        #FileLoc = File Location
    POETSD = ET.tostring(data, encoding="unicode")
    NewSongFile = open(FileName + '.xml', mode='w')
    NewSongFile.write(EncodeData)
    NewSongFile.write(POETSD)
    return
createXmlData(FilePath)
#POETSD = Post Element Tree Song Data

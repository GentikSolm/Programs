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
def FileSorter(FilePath):

    """
    SOLVED

    Create array of file paths that need to be moved, then move that array to specefied folder inside origin, then sort.
    also, Create folder in same area as specefied folder, then create its sub folders as needed as transfer of songs start.

    """





    tmpfolder = FilePath+"\\TMPSONGHOLD"
    shutil.rmtree(tmpfolder)
    os.mkdir(tmpfolder)
    for folderName, subfolders, filenames in os.walk(FilePath):
        loadBar(filenames)
        count = 0
        for file in filenames:
            count += percent
            if count >= 1:
                count = 0
                moveBar()
            #print(folderName+"\\"+file)
            if ".cdg" or ".mp3" in file:
                try:
                    shutil.move(folderName+"\\"+file,tmpfolder)
                except:
                    print("Moving of "+folderName+"\\"+file+ " Failed!")
    print("\nDone!")


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
    sys.stdout.write('\b->')
    sys.stdout.flush()

WhereFilePath()
FileSorter(FilePathInput)

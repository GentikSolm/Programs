#Declaring the global variables
width = 2
height = 1

#startup program
def startUp():
    print("Welcome to Josh's Staircase building program! \n Please input a positve number or type 'Help' for commands!")

def modHeight():
    print("What do you want the height to be?")
    global height
    height = input()
    #Comfirming isdigit
    if height.isdigit() and int(height) != 0:
        height = int(height)
        print("\nThe height is now {}!".format(height))
        return
    else:
        print("Please input a number greater than 0!")
        return

def modWidth():
    print("What do you want the width to be?")
    global width
    width = input()
    #Comfirming isdigit
    if width.isdigit() and int(width) != 0:
        width = int(width)
        print("\nThe Width is now {}!".format(width))
        return
    else:
        print("Please input a number greater than 0!")
        return

def helpComand():
    print("If you see '=>', the program is expecting a number to build a staircase.")
    print("\nHere are your commands:\nHelp\nExit\nWidth\nheight")
    return

#Deciding what comand to execute
def getInput(UserIn):
    #First call
    if UserIn == None:
        return True
    #Exit Script
    elif "exit" in UserIn.lower():
        return False
    #Help Script
    elif "help" in UserIn.lower():
        helpComand()
        return True
    #call Width Script
    elif "width" in UserIn.lower():
        modWidth()
        return True
    #call height Script
    elif "height" in UserIn.lower():
        modHeight()
        return True
    #Passing User input to the number checker
    else:
        numCheck(UserIn)
        return True
#Function that checks if input is type digit
def numCheck(inputType):
    if inputType.isdigit():
        finalNum = int(inputType)
        if finalNum == 0:
            print("Must be more than 1 stair!")
            return
        else:
            Stair(finalNum)
            return
    else:
        print("Please input a positive number!")
        return
#Stair Maker
def Stair(NumStairs):
    if NumStairs <= 0:
        print("Must be more than 1 stair!")
        return
    else:
        print("_"*(width+1))
        x = 0
        while NumStairs > x:
            x += 1
            #Excessivly complex math for a dynamic staircase!
            Step = x *((width + 1)*" ") + (( "|" + ((("\n"+((width+1)*x)*" ")+"|")*(height-1)))+("_"*width))
            print(Step)
        return


#Calls program into loop
startUp()
UserIn = None
while getInput(UserIn) == True:
    UserIn = input("\n=> ")

def goodbye():
    print("\nGoodbye!")
goodbye()

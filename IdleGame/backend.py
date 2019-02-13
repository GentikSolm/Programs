money = 0
moneyManipLevel = 0
moneyPC = 1
costRedLevel = 0
costRed = 0.00
unComp = None
compData = []
saveData = None
totalCosmet = 0
cosmets = ["->", "~>", "\\\\", "::", "$>", "|#>"]
currentCosmet = cosmets[0]
userInput = None
costRedPrice = ((costRedLevel+1)**2) * 1000
moneyPCPrice = (((moneyManipLevel+1)**2) *1000) * costRed
cosmetPrice = ((totalCosmet+1) **3 * 1000) * costRed

def startUp():
    with open("saveData.txt",mode='r') as Data:
        unComp = Data.read()
        global compData
        unComp = unComp.split(":")
        unComp.pop()
        #print(unComp)
        compData = [float(num) for num in unComp]
        global money
        global moneyManipLevel
        global moneyPC
        global costRedLevel
        money = compData[0]
        moneyManipLevel = compData[1]
        moneyPC = compData[2]
        costRedLevel = compData[3]
        costRed = compData[4]
        totalCosmet = compData[5]
def helpFunc():
    print("When in upgrades, the small number indicates what to type to activate that command. The second number is how much it will cost.")
    print("Here are the different commands:")
    commands = ["Help", "Upgrade", "Exit", "Money", "Restart", "Save"]
    for i in commands:
        print("{}".format(i))
def upgradeClick():
    global money
    global moneyPCPrice
    global moneyPC
    global moneyPCPrice
    if money >= moneyPCPrice:
        global moneyManipLevel
        money = money - moneyPCPrice
        moneyManipLevel += 1
        moneyPC = moneyManipLevel **2
        moneyPCPrice = (((moneyManipLevel+1)**2) *1000) * costRed
        print("You now earn {} per click!".format(moneyPC))
    else:
        print("You dont have enough money for that!")
def upgradeCostRed():
    global costRed
    global money
    global costRedLevel
    global costRedPrice
    if money >= costRedPrice and costRedLevel >= 5:
        money = money - costRedPrice
        costRedLevel += 1
        costRed = costRedLevel * .1
        costRedPrice = ((costRedLevel+1)**2) * 1000
    elif costRedLevel == 5:
        print("Youve reached max level here!")
    else:
        print("You dont have enough money!")
def upgradeCosmet():
    pass
def checkIn(userInput):
    if userInput == None:
        return True
    userInput = userInput.lower()
    if userInput == "exit":
        return False
    elif "upgrade" in userInput:
        question = input("What would you like to upgrade/buy?\nCosmetic(1)--{}\nHarder click(2)--{}\nCost reduction(3)--{}\n{} ".format(cosmetPrice, moneyPCPrice, costRedPrice, currentCosmet))
        if question == "1":
            upgradeCosmet()
        elif question == "2":
            upgradeClick()
        elif question == "3":
            upgradeCostRed()
        else:
            print("I dont understand what you were trying to buy!")
        return True
    elif 'help' in userInput:
        helpFunc()
        return True
    elif userInput == "money":
        print(money)
        print("You are making {} per click!".format(moneyPC))
        return True
    elif userInput == "restart":
        verify = input("Are you sure?\nYes\\No\n-> ")
        if verify.lower() == "yes":
            reset()
            print("Data reset!")
        else:
            print("Data not reset!")
        return True
    elif userInput == "cosmetic":
        chooseCosmet()
    elif userInput == "save":
        saveGameWithTxt()
        print("Game has been saved!")
        return True
    else:
        click()
        return True
def chooseCosmet():
    global currentCosmet
    print("You currently own {} cosmetics!".format(cosmets[0,totalCosmet]))
    whatCosmet = input("What icon set do you want to use? Please enter the number of the icon\n")
    int(whatCosmet)
    if whatCosmet-1 >= totalCosmet:
        currentCosmet = cosmets[whatCosmet-1]
    else:
        print("You dont own that!")
def click():
    global money
    money = money + moneyPC
def reset():
    with open("saveData.txt", mode="w") as resetData:
        resetData.write("0:0:1:0:0:1:")
    startUp()
def saveGameWithTxt():
    with open("saveData.txt", mode='w') as saveDataNew:
        compData = [money,moneyManipLevel,moneyPC,costRedLevel,costRed, totalCosmet]
        saveString = ""
        for i in compData:
            saveString = saveString + str(i) + ":"
        saveDataNew.write(saveString)
def closeDown():
    saveGameWithTxt()
    #saveGameWithPy()
    #saveGameWithJson()
    print("Goodbye!")
startUp()
while checkIn(userInput) == True:
    userInput = input(currentCosmet + " ")
closeDown()

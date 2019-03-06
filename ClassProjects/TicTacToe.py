nums = [1,2,3,4,5,6,7,8,9]
i = 1
toWinX = ["X","X","X"]
toWinO = ["O","O","O"]
def player():
    global i
    i += 1
    if i%2 == 0:
        a = "X"
    else:
        a = "O"
    return a
def getInput(P):
    while True:
        try:
            userIn = input(f"Player {P}, Enter your number!\n--> ")
            num = int(userIn)
        except ValueError:
            print("That was not a valid number! Please enter a new number!")
            num = None
        if num in screen:
            break
        elif num == None:
            pass
        else:
            print("That number is alrady in use or out of range! Enter a new number!")
    return [num,P]
def checkWin(screen):
    if screen[0:3] == toWinO or screen[3:6] == toWinO or screen[6:9] == toWinO or screen[0:7:3] == toWinO or screen[1:8:3] == toWinO or screen[2:9:3] == toWinO or screen[0:9:4] == toWinO or screen[2:7:2] == toWinO:
        return "O"
    elif screen[0:3] == toWinX or screen[3:6] == toWinX or screen[6:9] == toWinX or screen[0:7:3] == toWinX or screen[1:8:3] == toWinX or screen[2:9:3] == toWinX or screen[0:9:4] == toWinX or screen[2:7:2] == toWinX:
        return "X"
    else:
        for j in nums:
            if j in screen:
                return None
        else:
            return "TIE"
def printscreen(FScreen):

    screen[FScreen[0]-1] = FScreen[1]
    print(f"|{screen[0]}|{screen[1]}|{screen[2]}|\n-------\n|{screen[3]}|{screen[4]}|{screen[5]}|\n-------\n|{screen[6]}|{screen[7]}|{screen[8]}|\n")
    return screen
def endgame(winner):
    if winner == "TIE":
        print("The game has come to a tie")
        return
    else:
        print(f"{winner} Wins!")
def runGame():
    global screen
    screen = [1,2,3,4,5,6,7,8,9]
    print(f"Player 1 is X, and Player 2 is O, BEGIN!")
    print(f"|{screen[0]}|{screen[1]}|{screen[2]}|\n-------\n|{screen[3]}|{screen[4]}|{screen[5]}|\n-------\n|{screen[6]}|{screen[7]}|{screen[8]}|\n")
    while checkWin(screen) == None:
        person = player()
        change = getInput(person)
        screen = printscreen(change)
    else:
        endgame(checkWin(screen))
runGame()

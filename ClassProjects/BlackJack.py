import random
from CardDeck import Deck, Card
reference = {"Ace":11,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace1":1}
playgame = True

class Game():
    def hit(self):
        hitCard = myDeck.deck.pop()
        print("It was a " + hitCard.__str__())
        return hitCard

class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.currentBet = None
        self.notstaying = True
    def bet(self):
        try:
            betamm = int(input('How much do you want to bet?\n-> '))
        except:
            while True:
                try:
                    betamm = int(input('Please only input a number, how much do you want to bet?\n-> '))
                    break
                except:
                    pass
        while betamm > self.money:
            betamm = int(input(f'You only have {self.money}! How much do you want to bet?\n-> '))
        else:
            self.currentBet = betamm
    def stay(self):
        self.notstaying = False
    def win(self):
        userin = input(f'Congratulations you won {self.currentBet}! Would you like to play again?\n(y/n): ').lower()
        while userin != "y" and userin != "n":
            userin = input("I didn't get that, could you input that again?\n-> ").lower()
        if userin == "y":
            playagain = True
        elif userin == "n":
            playagain = False
        self.money += self.currentBet
        return playagain
    def lost(self):
        userin = input(f'Im sorry, you lost {self.currentBet}! Would you like to play again?\n(y/n): ').lower()
        while userin != "y" and userin != "n":
            userin = input("I didn't get that, could you input that again?\n-> ").lower()
        if userin == "y":
            playagain = True
        elif userin== "n":
            playagain = False
        self.money -= self.currentBet
        return playagain

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_cards(self,card):
        self.cards.append(card)
        self.value += reference[card.num]

    def adjust_for_ace(self,card):
        self.cards.append(card)
        ask = input("You got an ace! do you want 11 or 1?\n-> ")
        while ask != "1" and ask != "11":
            ask = input("Sorry i didn't get that, please enter 11 or 1!\n-> ")
        if ask == "11":
            self.value += 11
        else:
            self.value += 1
    def check21(self):
        if self.value < 21:
            return True
        else:
            return False
myGame = Game()
computer = Player("Comp", -1)
def initGame():
    name = input('Hello, What is your name?\n-> ').lower().capitalize()
    try:
        money = int(input(f'Hello {name}, how much money do you want to put into your account?\n-> '))
    except:
        while True:
            try:
                money = int(input('Please only input a number, how much do you want to put in?\n-> '))
                break
            except:
                pass
    return (name, money)
PlayN, PlayM = initGame()
player1 = Player(PlayN, PlayM)
print(f'Welcome {PlayN}!')
while playgame:
    myDeck = Deck()
    myDeck.shuffle()
    print(f'Your balance is ${player1.money}.')
    player1.bet()
    comphand = Hand()
    playerhand = Hand()
    while computer.notstaying or player1.notstaying:
        if player1.notstaying:
            print(f'-------\nYou are at a value of {playerhand.value}, and the computer is at a value of {comphand.value}')
            userin = input(f"{player1.name}, Your turn! Hit or stay?\n-> ")
            while userin.lower() != "hit" and userin.lower() != "stay":
                userin = input("Thats not a valid input, please enter again, Hit or stay.\n-> ")
            if userin.lower() == 'hit':
                card = myGame.hit()
                if card.num == "Ace":
                    playerhand.adjust_for_ace(card)
                else:
                    playerhand.add_cards(card)
                if playerhand.check21() == False:
                    player1.stay()
            else:
                player1.stay()
        if computer.notstaying:
            print("Computer's Turn!")
            if player1.notstaying == False and comphand.value <= playerhand.value and comphand.value < 18 or player1.notstaying == True and comphand.value <=14:
                card = myGame.hit()
                if card.num == "Ace":
                    if comphand.value <= 10:
                        comphand.add_cards(card)
                    else:
                        card.num = "Ace1"
                        comphand.add_cards(card)
                else:
                    comphand.add_cards(card)
                if comphand.check21() == False:
                    computer.stay()
            else:
                computer.stay()
                print("The computer stayed!")
    else:
        print(f'You have a final score of {playerhand.value}, and the computer has a score of {comphand.value}')
        if comphand.value > 21:
            playgame = player1.win()
        elif playerhand.value > 21:
            playgame = player1.lost()
        elif comphand.value > playerhand.value:
            playgame = player1.lost()
        elif comphand.value < playerhand.value:
            playgame = player1.win()
        elif comphand.value == playerhand.value:
            userin = input("There was a tie! Your bet was not lost nor gained. Play again?\n(y/n): ").lower()
            while  userin != "y" and userin != "n":
                userin = input("I didn't get that, could you input that again?\n-> ").lower()
            if userin == "y":
                playgame = True
            elif userin == "n":
                playgame = False
        del myDeck
        del comphand
        del playerhand
        computer.notstaying = True
        player1.notstaying = True
        if player1.money == 0:
            print("It seems you are broke!")
            playgame = False
print('Goodbye, and thanks for playing!')

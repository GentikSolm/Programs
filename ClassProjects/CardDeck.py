import random
types = ("Hearts","Clubs","Diamonds","Spades")
values = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
class Card():
    def __init__(self, type, num):
        self.type = type
        self.num = num
    def __str__(self):
        return self.num+" of "+self.type

class Deck():
    def __init__(self):
        self.deck = []
        for t in types:
            for v in values:
                self.deck.append(Card(t,v))
    def shuffle(self):
        random.shuffle(self.deck)
    def __str__(self):
        inDeck = ''
        for card in self.deck:
            inDeck += "\n"+card.__str__()
        return 'The deck has '+inDeck + " and a total of " + str(len(self.deck))+" Cards."
if __name__ == "__main__":
    testDeck = Deck()
    testDeck.shuffle()
    print(testDeck)

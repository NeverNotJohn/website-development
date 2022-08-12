from asyncio.windows_events import NULL
from random import randint, shuffle

class hand():

    def reshuffle(self):
        shuffle(self.discard)
        for i in range(len(self.discard)):
            self.cards.append(self.discard[i])
        self.discard = []

    def play(self):
        if (len(self.cards) == 0):
            self.reshuffle()
        num = randint(0, len(self.cards) - 1)
        self.activeCard = self.cards[num]

    def drawThree(self):
        for i in range(3):
            num = randint(0, len(self.cards))
            self.warRes.append(self.cards[num])
            del self.cards[num]
        

class deck(hand):

    def __init__(self):
        self.cards = "1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 13 13".split()
        shuffle(self.cards)
        for i in range(len(self.cards)):
            self.cards[i] = int(self.cards[i])

    def deal(self, user, comp):
        user.cards = [self.cards[i] for i in range(0, 26)]
        comp.cards = [self.cards[i] for i in range(26, 52)]

class player(hand):

    def __init__(self, name):
        self.discard = []
        self.cards = []
        self.activeCard = NULL
        self.warRes = []
        self.name = name
        print(f"Player {self.name} has joined")

def check(self, other):
        print(f"{self.name}'s cards: {self.cards}")
        print(f"{self.name}'s discard: {self.discard}")
        print(f"{self.name}'s warRes: {self.warRes}")
        print(f"{self.name}'s active: {self.activeCard}")
        print(f"{other.name}'s cards: {other.cards}")
        print(f"{other.name}'s discard: {other.discard}")
        print(f"{other.name}'s warRes: {other.warRes}")
        print(f"{other.name}'s active: {other.activeCard}")

def result(winner, loser):
    winner.discard.append(loser.activeCard)
    loser.cards.remove(loser.activeCard)
    winner.discard.append(winner.activeCard)
    winner.cards.remove(winner.activeCard)

    for i in range(len(loser.warRes)):
        winner.discard.append(winner.warRes[i])
        winner.discard.append(loser.warRes[i])
    winner.warRes = []
    loser.warRes = []

    
def round(user, comp):
    while (True):
        print(f"{user.name} has played {user.activeCard}!")
        print(f"{comp.name} has played {comp.activeCard}!")

        if (user.activeCard > comp.activeCard):
            print(f"{user.name} has won!")
            result(user, comp)
            break

        if (comp.activeCard > user.activeCard):
            print(f"{comp.name} has won! haha loser")
            result(comp, user)
            break

        if (comp.activeCard == user.activeCard):
            print(f"They are equal!!! TIME FOR WAR")
            
            comp.warRes.append(comp.activeCard)
            user.warRes.append(comp.activeCard)

            input("Press Enter to continue...")
            print(f"{user.name} has drawn three cards...")
            print(f"{comp.name} has drawn three cards... BUT COOLER")

            for i in range(3):
                if (len(user.cards) == 0):
                    user.reshuffle()
                num = randint(0, len(user.cards) - 1)
                user.warRes.append(user.cards[num])
                user.cards.remove(user.cards[num])

            for i in range(3):
                if (len(comp.cards) == 0):
                    comp.reshuffle()
                num = randint(0, len(comp.cards) - 1)
                comp.warRes.append(comp.cards[num])
                comp.cards.remove(comp.cards[num])

            comp.play()
            user.play()

def lossCheck(input):
    if ((len(input.warRes) == 0) and (len(input.cards) == 0) and (len(input.discard) == 0)):
        return True




        
dealer = deck()
user = player(input("Input name: "))
comp = player("Ima Beat Yu")

dealer.deal(user, comp)

while (True):
    user.play()
    comp.play()

    round(user, comp)

    input("Press Enter to continue...")

    if (lossCheck(user)):
        print("AHA U LOST LOSER")
        break

    elif (lossCheck(comp)):
        print(f"{user.name} YOU WON LEZ GO")

    print("\b \b")
from random import shuffle


print("WELCOME TO WAR")

pool = []

def getPool():
    return pool

deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
shuffle(deck)

userLoss = False
compLoss = False

class player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.active = 0
        print(f"{self.name} has joined the game!")

    def numCards(self):
        return len(self.hand)

    def playCard(self):
        checkWin()
        self.active = self.hand[0]
        pool.append(self.active)
        self.hand.pop(0)


user = player(input("Input name: "))
comp = player("Computer >:D")

for i in range(26):
    user.hand.append(deck.pop())
for i in range(26):
    comp.hand.append(deck.pop())

def showDown(user, comp):
    while (True):
        if (user.active > comp.active):

            pool = getPool()

            for i in range(len(pool)):
                user.hand.append(pool[i])
            print(f"{user.name} won!")
            break

        elif (comp.active > user.active):

            pool = getPool()

            for i in range(len(pool)):
                comp.hand.append(pool[i])
            print(f"{comp.name} won!")
            break

        elif (comp.active == user.active):
            print("ITS A WAR!")
            print("each user draws three cards")
            for i in range(4):
                checkWin()
                if(userLoss):
                    break
                if(compLoss):
                    break
                user.playCard()
                comp.playCard()

def checkWin():
    global userLoss
    global compLoss

    if (len(user.hand) == 0):
        userLoss = True
    if (len(comp.hand) == 0):
        compLoss = True

while (True):

    user.playCard()
    print(f"{user.name} plays {user.active}!")
    comp.playCard()
    print(f"{comp.name} plays {comp.active}!")

    print()

    showDown(user, comp)

    print()
    print()
    print(f"{comp.name} has {comp.numCards()} cards")
    print(f"{user.name} has {user.numCards()} cards")
    
    checkWin()
    pool = []


    if(userLoss):
        print(f"{comp.name} HAS WON U LOSER")
        break
    if(compLoss):
        print(f"{user.name} WON WOOOOOOT")
        break

    #debug:


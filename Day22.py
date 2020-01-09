inputString = open("Day22Input.txt").read().splitlines()
#inputString = ["deal with increment 7", "deal with increment 9", "cut -2"]
deck = list(range(10007))

def modifyDeck(technique):
    global deck
    if technique == "deal into new stack":
        deck.reverse()
    if "cut" in technique:
        amount = int(technique.split(" ")[1])
        deck = deck[amount:] + deck[:amount]
    if "deal with increment" in technique:
        increment = int(technique.split("increment ")[1])
        currentPos = 0
        newDeck = [0] * len(deck)
        while len(deck) > 0:
            newDeck[currentPos % len(newDeck)] = deck.pop(0)
            currentPos += increment
        deck = newDeck


def partOne():
    for techinque in inputString:
        modifyDeck(techinque)
    print(deck.index(2019))

partOne()
import math
inputString = open("Day14Input.txt").read().splitlines()

reactions = {}

def parseInput():
    for item in inputString:
        product = item.split(" => ")[1].split(" ")[1]
        numProduct = int(item.split(" => ")[1].split(" ")[0])
        resources = []
        if item.split(" => ")[0].find(", ") > 0:
            for resource in item.split(" => ")[0].split(", "):
                resources.append([resource.split(" ")[1], int(resource.split(" ")[0])])
        else:
            resources.append([item.split(" => ")[0].split(" ")[1], int(item.split(" => ")[0].split(" ")[0])])
        reactions[product] = [numProduct, resources]

def findClosestMultiplier(amount, multiplier, realNumber):
    if realNumber:
        return amount/multiplier, ((amount/multiplier)*multiplier)-amount
    else:
        return math.ceil(amount / multiplier), (math.ceil(amount / multiplier) * multiplier) - amount

#amount is already a multiple of the reaction output
def makeItem(what, multiplier):
    output = []
    for item in reactions[what][1]:
        output.append([item[0], item[1]*multiplier])
    return output

def findElements(what, amount, realNumber):
    elementList = {}
    intermediary = {what: amount}
    leftovers = {}
    while len(intermediary) > 0:
        newIntermediary = {}
        for item in intermediary.copy():
            multiplier = findClosestMultiplier(intermediary[item], reactions[item][0], realNumber)
            parts = makeItem(item, multiplier[0])
            if multiplier[1] > 0:
                if item in leftovers.keys():
                    leftovers[item] += multiplier[1]
                else:
                    leftovers[item] = multiplier[1]
            intermediary.pop(item)
            for reactionItem in parts:
                if reactions[reactionItem[0]][1][0][0] == "ORE":
                    if reactionItem[0] in elementList.keys():
                        elementList[reactionItem[0]] += reactionItem[1]
                    else:
                        elementList[reactionItem[0]] = reactionItem[1]
                else:
                    if reactionItem[0] in newIntermediary.keys():
                        newIntermediary[reactionItem[0]] += reactionItem[1]
                    else:
                        newIntermediary[reactionItem[0]] = reactionItem[1]
        for item in newIntermediary:
            if item in leftovers.keys():
                if newIntermediary[item] >= leftovers[item]:
                    newIntermediary[item] -= leftovers[item]
                    leftovers.pop(item)
                else:
                    leftovers[item] -= newIntermediary[item]
                    newIntermediary[item] = 0
        intermediary = newIntermediary
    return calculateOreNeededForElements(elementList, realNumber)

def calculateOreNeededForElements(listOfElements, realNumber):
    totalOre = 0
    for element in listOfElements:
        totalOre += makeItem(element, findClosestMultiplier(listOfElements[element], reactions[element][0], realNumber)[0])[0][1]
    return totalOre

def partOne():
    print(findElements("FUEL", 1, False))

def partTwo(oreInHold):
    oneRun = findElements("FUEL", 1, True)
    oreLeft = oreInHold - oneRun
    #add one because we already did one run
    fuelProduced = math.floor(oreLeft / oneRun) + 1
    oreLeft -= findElements("FUEL", math.floor(oreLeft/oneRun), True)
    while oreLeft > 0:
        oreLeft -= findElements("FUEL", 1, True)
        if oreLeft > 0:
            fuelProduced += 1
    print(fuelProduced)

parseInput()
partOne()
partTwo(1000000000000)

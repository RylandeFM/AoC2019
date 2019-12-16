inputString = open("Day16Input.txt").read()
#inputString = "80871224585914546619083218645595"
inputList = []
basePattern = [0, 1, 0, -1]

def parseInput():
    global inputList
    inputList = []
    for c in inputString:
        inputList.append(int(c))

def calcNewSum(position):
    offset = position
    step = position + 1
    output = 0
    while offset < len(inputList):
        output += sum(inputList[offset:offset + step])
        offset += 2 * step

        output -= sum(inputList[offset:offset + step])
        offset += 2 * step
    return abs(output) % 10

def runPartialPhase(repeats):
    global inputList
    length = len(inputList)
    for _ in range(repeats):
        newList = [0] * length
        newList[length-1] = inputList[length-1]
        for i in range(length - 2, length // 2, -1):
            dataElement = inputList[i]
            result = dataElement + newList[i + 1]
            newList[i] = result % 10
        inputList = newList

def runPhases(repeats):
    global inputList
    for _ in range(repeats):
        newList = []
        for i in range(len(inputString)):
            newList.append(calcNewSum(i))
        inputList = newList

def partOne():
    parseInput()
    runPhases(100)
    print("".join(str(x) for x in inputList[:8]))

def partTwo():
    global inputList
    parseInput()
    offset = int(inputString[:7])
    inputList = inputList * 10000
    runPartialPhase(100)
    print("".join(str(x) for x in inputList[offset:offset+8]))

partTwo()
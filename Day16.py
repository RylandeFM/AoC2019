inputString = open("Day16Input.txt").read()
#inputString = "80871224585914546619083218645595"
inputList = []
basePattern = [0, 1, 0, -1]

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

def processPhase():
    global inputList
    newList = []
    for i in range(len(inputString)):
        newList.append(calcNewSum(i))
    inputList = newList

def runPhases(repeats):
    for _ in range(repeats):
        processPhase()

runPhases(100)
print("".join(str(x) for x in inputList[:8]))

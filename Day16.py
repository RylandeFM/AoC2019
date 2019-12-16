inputString = open("Day16Input.txt").read()
#inputString = "19617804207202209144916044189917"
inputList = []
basePattern = [0, 1, 0, -1]

for c in inputString:
    inputList.append(int(c))

def expandPattern(multiplier):
    newPattern = []
    currentStep = 0
    currentAdd = 0
    for i in range(len(inputList)+1):
        newPattern.append(basePattern[currentStep % len(basePattern)])
        currentAdd += 1
        if currentAdd == multiplier:
            currentAdd = 0
            currentStep += 1
    newPattern = newPattern[1:]
    return newPattern

def applyPattern(input, pattern):
    output = 0
    for i in range(len(input)):
        output += input[i] * pattern[i]
    return int(str(output)[len(str(output))-1:])

def processPhase():
    global inputList
    newList = []
    for i in range(1, len(inputString)+1):
        newList.append(applyPattern(inputList, expandPattern(i)))
    inputList = newList

def runPhases(repeats):
    for j in range(repeats):
        processPhase()

runPhases(100)
print("".join(str(x) for x in inputList[:8]))
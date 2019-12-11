program = open("Day11Input.txt").read()

#x, y, mode
currentPosition = [0, 0, 0]
output = [0, 0]
modeList = ['U', 'R', 'D', 'L']
paintedSquares = {}

def readProgram(programString):
    programList = programString.split(',')
    memory = {}
    for index in range(len(programList)):
        memory[index] = programList[index]
    return memory

def computeProgram(baseColor):
    #initialize variables
    global currentPosition
    paintedSquares[(0, 0)] = baseColor
    currentPosition = [0, 0, 0]
    index = 0
    relativeIndex = 0
    currentOutput = 0
    programArray = readProgram(program)

    while int(programArray[index]) != 99:
        opcode = str(programArray[index]).zfill(5)
        if int(opcode[2]) == 1:
            n1 = 0 if index + 1 not in programArray.keys() else int(programArray[index + 1])
        elif int(opcode[2]) == 0:
            n1 = 0 if int(programArray[index + 1]) not in programArray.keys() else int(programArray[int(programArray[index + 1])])
        else:
            n1 = 0 if int(programArray[index + 1]) + relativeIndex not in programArray.keys() else int(programArray[int(programArray[index + 1]) + relativeIndex])

        if int(opcode[4]) != 4 and int(opcode[4]) != 3 and int(opcode[4]) != 9:
            if int(opcode[1]) == 1:
                n2 = 0 if index + 2 not in programArray.keys() else int(programArray[index + 2])
            elif int(opcode[1]) == 0:
                n2 = 0 if int(programArray[index + 2]) not in programArray.keys() else int(programArray[int(programArray[index + 2])])
            else:
                n2 = 0 if int(programArray[index + 2]) + relativeIndex not in programArray.keys() else int(programArray[int(programArray[index + 2]) + relativeIndex])

        if int(opcode[4]) == 1:
            if int(opcode[0]) == 2:
                programArray[int(programArray[index + 3]) + relativeIndex] = n1 + n2
            else:
                programArray[int(programArray[index+3])] = n1 + n2
            index += 4
        elif int(opcode[4]) == 2:
            if int(opcode[0]) == 2:
                programArray[int(programArray[index + 3]) + relativeIndex] = n1 * n2
            else:
                programArray[int(programArray[index+3])] = n1 * n2
            index += 4
        elif int(opcode[4]) == 3:
            if (currentPosition[0], currentPosition[1]) not in paintedSquares.keys():
                color = baseColor
            else:
                color = paintedSquares[(currentPosition[0], currentPosition[1])]
            if int(opcode[2]) == 2:
                programArray[int(programArray[index + 1]) + relativeIndex] = color
            else:
                programArray[int(programArray[index + 1])] = color
            index += 2
        elif int(opcode[4]) == 4:
            output[currentOutput % 2] = n1
            currentOutput += 1
            moveRobot(currentOutput % 2)
            index += 2
        elif int(opcode[4]) == 5:
            index = n2 if n1 != 0 else index + 3
        elif int(opcode[4]) == 6:
            index = n2 if n1 == 0 else index + 3
        elif int(opcode[4]) == 7:
            if int(opcode[0]) == 2:
                programArray[int(programArray[index + 3]) + relativeIndex] = 1 if n1 < n2 else 0
            else:
                programArray[int(programArray[index + 3])] = 1 if n1 < n2 else 0
            index += 4
        elif int(opcode[4]) == 8:
            if int(opcode[0]) == 2:
                programArray[int(programArray[index + 3]) + relativeIndex] = 1 if n1 == n2 else 0
            else:
                programArray[int(programArray[index + 3])] = 1 if n1 == n2 else 0
            index += 4
        elif int(opcode[4]) == 9:
            relativeIndex += n1
            index += 2
        else:
            print("error")
            return 0

def moveRobot(mode):
    if mode == 1:
        paintedSquares[(currentPosition[0], currentPosition[1])] = output[0]
    elif mode == 0:
        if output[1] == 0:
            currentPosition[2] = (currentPosition[2] - 1) % 4
        else:
            currentPosition[2] = (currentPosition[2] + 1) % 4

        if modeList[currentPosition[2]] == 'U':
            currentPosition[1] += 1
        elif modeList[currentPosition[2]] == 'D':
            currentPosition[1] -= 1
        elif modeList[currentPosition[2]] == 'L':
            currentPosition[0] -= 1
        elif modeList[currentPosition[2]] == 'R':
            currentPosition[0] += 1

def printImage(image):
    for line in image:
        print("".join(line))

def visualizePaintedSquares():
    #minX, maxX, minY, maxY
    borders = [0,0,0,0]
    squaresToPaint = []
    for coord in paintedSquares.keys():
        if paintedSquares[coord] == 1:
            squaresToPaint.append(coord)
            borders[0] = min(borders[0], coord[0])
            borders[1] = max(borders[1], coord[0])
            borders[2] = min(borders[2], coord[1])
            borders[3] = max(borders[3], coord[1])
    image = [[' ' for j in range(abs(borders[1]-borders[0])+1)] for i in range(abs(borders[3]-borders[2])+1)]
    for square in squaresToPaint:
        image[abs(square[1])][square[0]] = "#"
    printImage(image)

computeProgram(0)
print(len(paintedSquares))
paintedSquares = {}
computeProgram(1)
visualizePaintedSquares()
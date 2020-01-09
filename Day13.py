program = open("Day13Input.txt").read()

tiles = {}
ball = ()
paddle = ()

def readProgram(programString):
    programList = programString.split(',')
    memory = {}
    for index in range(len(programList)):
        memory[index] = int(programList[index])
    return memory

def computeProgram(input):
    #initialize variables
    score = 0
    index = 0
    relativeIndex = 0
    memory = readProgram(program)
    currentTile = [0] * 3
    tileIndex = 0

    memory[0] = input
    while memory[index] != 99:
        opcode = str(memory[index]).zfill(5)
        if int(opcode[2]) == 1:
            n1 = 0 if index + 1 not in memory.keys() else memory[index + 1]
        elif int(opcode[2]) == 0:
            n1 = 0 if memory[index + 1] not in memory.keys() else memory[memory[index + 1]]
        else:
            n1 = 0 if memory[index + 1] + relativeIndex not in memory.keys() else memory[
                memory[index + 1] + relativeIndex]

        if int(opcode[4]) != 4 and int(opcode[4]) != 3 and int(opcode[4]) != 9:
            if int(opcode[1]) == 1:
                n2 = 0 if index + 2 not in memory.keys() else memory[index + 2]
            elif int(opcode[1]) == 0:
                n2 = 0 if memory[index + 2] not in memory.keys() else memory[memory[index + 2]]
            else:
                n2 = 0 if memory[index + 2] + relativeIndex not in memory.keys() else memory[
                    memory[index + 2] + relativeIndex]

        if int(opcode[4]) == 1:
            if int(opcode[0]) == 2:
                memory[memory[index + 3] + relativeIndex] = n1 + n2
            else:
                memory[memory[index + 3]] = n1 + n2
            index += 4
        elif int(opcode[4]) == 2:
            if int(opcode[0]) == 2:
                memory[memory[index + 3] + relativeIndex] = n1 * n2
            else:
                memory[memory[index + 3]] = n1 * n2
            index += 4
        elif int(opcode[4]) == 3:
            if ball[0] > paddle[0]:
                joystickPosition = 1
            elif ball[0] < paddle[0]:
                joystickPosition = -1
            else:
                joystickPosition = 0

            if int(opcode[2]) == 2:
                memory[memory[index + 1] + relativeIndex] = joystickPosition
            else:
                memory[memory[index + 1]] = joystickPosition
            index += 2
        elif int(opcode[4]) == 4:
            currentTile[tileIndex % 3] = n1
            tileIndex += 1
            if tileIndex % 3 == 0:
                if currentTile[0] == -1 and currentTile[1] == 0:
                    score = currentTile[2]
                else:
                    if currentTile[2] == 3:
                        paddle = (currentTile[0], currentTile[1])
                    elif currentTile[2] == 4:
                        ball = (currentTile[0], currentTile[1])
                    else:
                        tiles[(currentTile[0], currentTile[1])] = currentTile[2]
                currentTile = [0, 0, 0]
            index += 2
        elif int(opcode[4]) == 5:
            index = n2 if n1 != 0 else index + 3
        elif int(opcode[4]) == 6:
            index = n2 if n1 == 0 else index + 3
        elif int(opcode[4]) == 7:
            if int(opcode[0]) == 2:
                memory[memory[index + 3] + relativeIndex] = 1 if n1 < n2 else 0
            else:
                memory[memory[index + 3]] = 1 if n1 < n2 else 0
            index += 4
        elif int(opcode[4]) == 8:
            if int(opcode[0]) == 2:
                memory[memory[index + 3] + relativeIndex] = 1 if n1 == n2 else 0
            else:
                memory[memory[index + 3]] = 1 if n1 == n2 else 0
            index += 4
        elif int(opcode[4]) == 9:
            relativeIndex += n1
            index += 2
        else:
            print("error")
            return 0
    return score

def partOne():
    computeProgram(1)
    counter = 0
    for tile in tiles.values():
        if tile == 2:
            counter += 1
    print(counter)

def partTwo():
    print(computeProgram(2))

partOne()
partTwo()

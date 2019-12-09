program = open("Day9Input.txt").read().splitlines()
#program = ["1102,10,2,1985,109,2000,109,19,204,-34,203,-34,204,-34,99"]

def computeProgram(input):
    programArray = readProgram(program[0])
    index = 0
    relativeIndex = 0
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
            if int(opcode[2]) == 2:
                programArray[int(programArray[index + 1]) + relativeIndex] = input
            else:
                programArray[int(programArray[index + 1])] = input
            index += 2
        elif int(opcode[4]) == 4:
            print(n1)
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

def readProgram(programString):
    programList = programString.split(',')
    memory = {}
    for index in range(len(programList)):
        memory[index] = programList[index]
    return memory

computeProgram(1)
computeProgram(2)

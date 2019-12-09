inputString = open("Day5Input.txt").read().splitlines()

def computeString(systemID):
    programArray = inputString[0].split(",")
    index = 0
    while int(programArray[index]) != 99:
        opcode = str(programArray[index]).zfill(5)
        n1 = int(programArray[index + 1]) if int(opcode[2]) == 1 else int(programArray[int(programArray[index + 1])])
        if int(opcode[4]) != 4:
            n2 = int(programArray[index + 2]) if int(opcode[1]) == 1 else int(programArray[int(programArray[index + 2])])

        if int(opcode[4]) == 1:
            programArray[int(programArray[index+3])] = n1 + n2
            index += 4
        elif int(opcode[4]) == 2:
            programArray[int(programArray[index+3])] = n1 * n2
            index += 4
        elif int(opcode[4]) == 3:
            programArray[int(programArray[index+1])] = systemID
            index += 2
        elif int(opcode[4]) == 4:
            print(n1)
            index += 2
        elif int(opcode[4]) == 5:
            index = n2 if n1 != 0 else index + 3
        elif int(opcode[4]) == 6:
            index = n2 if n1 == 0 else index + 3
        elif int(opcode[4]) == 7:
            programArray[int(programArray[index + 3])] = 1 if n1 < n2 else 0
            index += 4
        elif int(opcode[4]) == 8:
            programArray[int(programArray[index + 3])] = 1 if n1 == n2 else 0
            index += 4
        else:
            print("error")
            break
    return programArray[0]

computeString('1')
computeString('5')
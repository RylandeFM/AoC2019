inputString = open("Day5Input.txt").read()

def computeString(systemID):
    memory = [int(i) for i in inputString.split(",")]
    index = 0
    while memory[index] != 99:
        opcode = str(memory[index]).zfill(5)
        n1 = memory[index + 1] if int(opcode[2]) == 1 else memory[memory[index + 1]]
        if int(opcode[4]) != 4:
            n2 = memory[index + 2] if int(opcode[1]) == 1 else memory[memory[index + 2]]

        if int(opcode[4]) == 1:
            memory[memory[index + 3]] = n1 + n2
            index += 4
        elif int(opcode[4]) == 2:
            memory[memory[index + 3]] = n1 * n2
            index += 4
        elif int(opcode[4]) == 3:
            memory[memory[index + 1]] = systemID
            index += 2
        elif int(opcode[4]) == 4:
            print(n1)
            index += 2
        elif int(opcode[4]) == 5:
            index = n2 if n1 != 0 else index + 3
        elif int(opcode[4]) == 6:
            index = n2 if n1 == 0 else index + 3
        elif int(opcode[4]) == 7:
            memory[memory[index + 3]] = 1 if n1 < n2 else 0
            index += 4
        elif int(opcode[4]) == 8:
            memory[memory[index + 3]] = 1 if n1 == n2 else 0
            index += 4
        else:
            print("error")
            break
    return memory[0]

computeString(1)
computeString(5)
import itertools
import threading
import time

program = open("Day7Input.txt").read()
#program = ["3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"]
inputs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def computeProgram(inputID, outputID):
    currentInput = 0
    memory = [int(i) for i in program.split(",")]
    index = 0
    while memory[index] != 99:
        opcode = str(memory[index]).zfill(5)
        n1 = memory[index + 1] if int(opcode[2]) == 1 else memory[memory[index + 1]]
        if int(opcode[4]) != 4 and int(opcode[4]) != 3:
            n2 = memory[index + 2] if int(opcode[1]) == 1 else memory[memory[index + 2]]

        if int(opcode[4]) == 1:
            memory[memory[index+3]] = n1 + n2
            index += 4
        elif int(opcode[4]) == 2:
            memory[memory[index+3]] = n1 * n2
            index += 4
        elif int(opcode[4]) == 3:
            #If input not yet known, wait for it
            while inputs[inputID][0] != currentInput:
                time.sleep(0.001)
            memory[memory[index+1]] = inputs[inputID][1]
            index += 2
            currentInput += 1
        elif int(opcode[4]) == 4:
            inputs[outputID] = [inputs[outputID][0]+1, n1]
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
            return 0

def runPhaseSetting(phaseSettingList):
    index = 0
    for phase in phaseSettingList:
        inputs[index][1] = phase
        index += 1
    ampA = threading.Thread(target=computeProgram, args=(0, 1), daemon=True)
    ampA.start()
    ampB = threading.Thread(target=computeProgram, args=(1, 2), daemon=True)
    ampB.start()
    ampC = threading.Thread(target=computeProgram, args=(2, 3), daemon=True)
    ampC.start()
    ampD = threading.Thread(target=computeProgram, args=(3, 4), daemon=True)
    ampD.start()
    ampE = threading.Thread(target=computeProgram, args=(4, 0), daemon=True)
    ampE.start()

    #make sure amp A has a chance to pick up phase before initial input
    time.sleep(0.002)
    inputs[0] = [1, 0]
    ampE.join()
    return inputs[0][1]

def getMaxSignal(permutationList):
    phaseSettings = list(itertools.permutations(permutationList))
    maxOutput = 0
    for phaseSetting in phaseSettings:
        global inputs
        inputs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        currentOutput = runPhaseSetting(phaseSetting)
        if currentOutput > maxOutput:
            maxOutput = currentOutput
            highestPhase = phaseSetting
    print(highestPhase)
    return maxOutput

print(getMaxSignal([0, 1, 2, 3, 4]))
print(getMaxSignal([5, 6, 7, 8, 9]))

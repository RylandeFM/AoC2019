inputString = open("Day2Input.txt").read().splitlines()

def computeString(settingOne, settingTwo):
    programArray = inputString[0].split(",")
    programArray[1] = settingOne
    programArray[2] = settingTwo
    index = 0
    while int(programArray[index]) != 99:
        if int(programArray[index]) == 1:
            programArray[int(programArray[index+3])] = int(programArray[int(programArray[index+1])]) + int(programArray[int(programArray[index+2])])
        elif int(programArray[index]) == 2:
            programArray[int(programArray[index+3])] = int(programArray[int(programArray[index+1])]) * int(programArray[int(programArray[index+2])])
        else:
            print("error")
        index += 4
    return programArray[0]

print(computeString(12, 2))

for noun in range(99):
    for verb in range(99):
        if computeString(noun, verb) == 19690720:
            print(100*noun+verb)
            break

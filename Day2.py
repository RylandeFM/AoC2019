inputString = open("Day2Input.txt").read()

def computeString(settingOne, settingTwo):
    memory = [int(i) for i in inputString.split(",")]
    memory[1] = settingOne
    memory[2] = settingTwo
    index = 0
    while memory[index] != 99:
        if memory[index] == 1:
            memory[memory[index+3]] = memory[memory[index+1]] + memory[memory[index+2]]
        elif memory[index] == 2:
            memory[memory[index+3]] = memory[memory[index+1]] * memory[memory[index+2]]
        else:
            print("error")
        index += 4
    return memory[0]

print(computeString(12, 2))

resultFound = False
for noun in range(99):
    for verb in range(99):
        if computeString(noun, verb) == 19690720:
            print(100 * noun + verb)
            resultFound = True
            break
    if resultFound:
        break

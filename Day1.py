import math
inputString = open("Day1Input.txt", "r").read().splitlines()

def calculateMass(inputMass):
    return math.floor(int(inputMass)/3)-2

def partOne():
    totalFuel = 0
    for partMass in inputString:
        totalFuel += calculateMass(partMass)
    print(totalFuel)

def partTwo():
    for partMass in inputString:
        fuelRequired = calculateMass(partMass)
        totalFuel = fuelRequired
        while fuelRequired > 0:
            fuelRequired = calculateMass(fuelRequired)
            if fuelRequired > 0:
                totalFuel += fuelRequired
    print(totalFuel)

partOne()
partTwo()
import math
inputString = open("Day12Input.txt").read().splitlines()

moons = []
vectors = []
indexes = set()

def parseInput():
    index = 0
    for moon in inputString:
        moons.append([int(moon.split(',')[0].split('=')[1]), int(moon.split(',')[1].split('=')[1]), int(moon.split(',')[2].split('=')[1].replace(">",""))])
        vectors.append([0, 0, 0])
        indexes.add(index)
        index += 1

def updateVectors():
    for moonIndex in indexes:
        for secondMoonIndex in indexes.difference({moonIndex}):
            updateVectorPosition(moonIndex, secondMoonIndex, 0)
            updateVectorPosition(moonIndex, secondMoonIndex, 1)
            updateVectorPosition(moonIndex, secondMoonIndex, 2)

def updateVectorPosition(index1, index2, position):
    if moons[index1][position] > moons[index2][position]:
        vectors[index1][position] -= 1
    elif moons[index1][position] < moons[index2][position]:
        vectors[index1][position] += 1

def applyVectors():
    for moonIndex in indexes:
        moons[moonIndex][0] += vectors[moonIndex][0]
        moons[moonIndex][1] += vectors[moonIndex][1]
        moons[moonIndex][2] += vectors[moonIndex][2]

def calculateEnergy():
    totalEnergy = 0
    for index in range(len(moons)):
        totalEnergy += (abs(moons[index][0])+abs(moons[index][1])+abs(moons[index][2]))*(abs(vectors[index][0])+abs(vectors[index][1])+abs(vectors[index][2]))
    return totalEnergy

def getCoordinates(position):
    return (moons[0][position],vectors[0][position],moons[1][position],vectors[1][position],moons[2][position],vectors[2][position],moons[3][position],vectors[3][position])

def partOne(steps):
    for step in range(steps):
        updateVectors()
        applyVectors()
    print(calculateEnergy())

def partTwo():
    periodX = 0
    periodY = 0
    periodZ = 0
    steps = 0
    Xs = {getCoordinates(0)}
    Ys = {getCoordinates(1)}
    Zs = {getCoordinates(2)}
    while periodX == 0 or periodY == 0 or periodZ == 0:
        updateVectors()
        applyVectors()
        steps += 1
        coord = getCoordinates(0)
        if coord in Xs:
            periodX = steps
        coord = getCoordinates(1)
        if coord in Ys:
            periodY = steps
        coord = getCoordinates(2)
        if coord in Zs:
            periodZ = steps
    lcmXY = (periodX * periodY)//math.gcd(periodX, periodY)
    lcm = (lcmXY * periodZ)//math.gcd(lcmXY, periodZ)
    print(lcm)

parseInput()
partOne(1000)
parseInput()
partTwo()

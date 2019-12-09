inputString = open("Day3Input.txt").read().splitlines()
grid = {}
intersections = []

def traceWires():
    origin = "0,0,0"
    currentWire = 1
    for wireInput in inputString:
        currentCoord = origin
        currentSteps = 0
        for command in wireInput.split(","):
            cXY = currentCoord.split(",")
            currentSteps += int(cXY[2])
            currentCoord = processCommandSteps(command, int(cXY[0]), int(cXY[1]), str(currentWire), currentSteps)
        currentWire += 1

def processCommandSteps(command, currentX, currentY, ID, step):
    steps = int(command[1:])
    cStep = step
    coord = ""

    if command[0] == "D":
        for cY in range(currentY + 1, currentY + steps + 1):
            cStep += 1
            if str(cY)+","+str(currentX) in grid.keys():
                if grid[str(cY)+","+str(currentX)][0] != ID:
                    intersections.append(str(currentX)+','+str(cY)+','+str(cStep+int(grid[str(cY)+","+str(currentX)][1])))
            else:
                grid[str(cY)+","+str(currentX)] = [ID, cStep]
        coord = str(currentX)+","+str(currentY+steps)+","+str(steps)
    elif command[0] == "U":
        for cY in range(currentY-1, currentY - steps -1, -1):
            cStep += 1
            if str(cY)+","+str(currentX) in grid.keys():
                if grid[str(cY)+","+str(currentX)][0] != ID:
                    intersections.append(str(currentX) + ',' + str(cY)+','+str(cStep+int(grid[str(cY)+","+str(currentX)][1])))
            else:
                grid[str(cY)+","+str(currentX)] = [ID, cStep]
        coord = str(currentX) + "," + str(currentY - steps)+","+str(steps)
    elif command[0] == "L":
        for cX in range(currentX-1, currentX-1 - steps, -1):
            cStep += 1
            if str(currentY)+","+str(cX) in grid.keys():
                if grid[str(currentY)+","+str(cX)][0] != ID:
                    intersections.append(str(cX) + ',' + str(currentY)+','+str(cStep+int(grid[str(currentY)+","+str(cX)][1])))
            else:
                grid[str(currentY)+","+str(cX)] = [ID, cStep]
        coord = str(currentX - steps) + "," + str(currentY)+","+str(steps)
    elif command[0] == "R":
        for cX in range(currentX + 1, currentX + steps + 1):
            cStep += 1
            if str(currentY) + "," + str(cX) in grid.keys():
                if grid[str(currentY) + "," + str(cX)][0] != ID:
                    intersections.append(
                        str(cX) + ',' + str(currentY) + ',' + str(cStep + int(grid[str(currentY) + "," + str(cX)][1])))
            else:
                grid[str(currentY) + "," + str(cX)] = [ID, cStep]
        coord = str(currentX + steps) + "," + str(currentY)+","+str(steps)
    return coord


def findDistance(origin, intersection):
    oXY = origin.split(",")
    iXY = intersection.split(",")
    return abs(int(oXY[0])-int(iXY[0]))+abs(int(oXY[1])-int(iXY[1]))

def partOne():
    origin = "0,0,0"
    lowestDistance = 999999
    for intersect in intersections:
        currentDistance = findDistance(origin, intersect)
        if currentDistance < lowestDistance:
            lowestDistance = currentDistance
    print(lowestDistance)

def partTwo():
    currentLowest = 999999
    for intersect in intersections:
        currentSteps = int(intersect.split(',')[2])
        if currentSteps < currentLowest:
            currentLowest = currentSteps
    print(currentLowest)

traceWires()
partOne()
partTwo()

inputString = open("Day10Input.txt").read().splitlines()
#inputString = ['.#..#','.....','#####','....#','...##']
asteroids = set()
baseLocation = ()
visibleAsteroids = set()

def getAsteroids():
    for y in range(len(inputString)):
        for x in range(len(inputString[0])):
            if inputString[y][x] == '#':
                asteroids.add((x, y))

def countVisibleAsteroids(origin, potentials):
    QPP = set()
    QPN = set()
    QNP = set()
    QNN = set()
    U = False
    D = False
    L = False
    R = False
    numberVisible = 0
    for asteroid in potentials:
        relativeCoord = [int(asteroid[0])-int(origin[0]), int(asteroid[1])-int(origin[1])]
        #Asteroid on same X-axis
        if relativeCoord[0] == 0:
            if relativeCoord[1] > 0 and not U:
                numberVisible += 1
                U = True
            elif relativeCoord[1] < 0 and not D:
                numberVisible += 1
                D = True
        #Asteroid on same Y-Axis
        elif relativeCoord[1] == 0:
            if relativeCoord[0] > 0 and not R:
                numberVisible += 1
                R = True
            elif relativeCoord[0] < 0 and not L:
                numberVisible += 1
                L = True
        else:
            if relativeCoord[0] > 0 and relativeCoord[1] > 0:
                if relativeCoord[1]/relativeCoord[0] not in QPP:
                    numberVisible += 1
                    QPP.add(relativeCoord[1] / relativeCoord[0])
            elif relativeCoord[0] > 0 and relativeCoord[1] < 0:
                if relativeCoord[1]/relativeCoord[0] not in QPN:
                    numberVisible += 1
                    QPN.add(relativeCoord[1] / relativeCoord[0])
            elif relativeCoord[0] < 0 and relativeCoord[1] > 0:
                if relativeCoord[1]/relativeCoord[0] not in QNP:
                    numberVisible += 1
                    QNP.add(relativeCoord[1] / relativeCoord[0])
            elif relativeCoord[0] < 0 and relativeCoord[1] < 0:
                if relativeCoord[1]/relativeCoord[0] not in QNN:
                    numberVisible += 1
                    QNN.add(relativeCoord[1] / relativeCoord[0])
    return numberVisible

def orderAsteroidsByGradient(origin, potentials):
    True


def partOne():
    maxViewed = 0
    global baseLocation
    for rock in asteroids:
        currentViewed = countVisibleAsteroids(rock, asteroids)
        if currentViewed > maxViewed:
            maxViewed = currentViewed
            baseLocation = rock
    print(maxViewed)



getAsteroids()
partOne()
asteroids.remove(baseLocation)
#orderAsteroidsByGradient(baseLocation,asteroids.remove(baseLocation))
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
    QPP = {}
    QPN = {}
    QNP = {}
    QNN = {}
    U = []
    D = []
    L = []
    R = []
    relativeList = []
    for asteroid in potentials:
        relativeCoord = [int(asteroid[0])-int(origin[0]), int(origin[1])-int(asteroid[1])]
        #Asteroid on same X-axis
        if relativeCoord[0] == 0:
            if relativeCoord[1] > 0:
                if len(U) == 0:
                    U = relativeCoord
                elif U[0]+U[1] > relativeCoord[0]+relativeCoord[1]:
                    U = relativeCoord
            elif relativeCoord[1] < 0:
                if len(D) == 0:
                    D = relativeCoord
                elif D[0]+D[1] > relativeCoord[0]+relativeCoord[1]:
                    D = relativeCoord
        #Asteroid on same Y-Axis
        elif relativeCoord[1] == 0:
            if relativeCoord[0] > 0:
                if len(R) == 0:
                    R = relativeCoord
                elif R[0]+R[1] > relativeCoord[0]+relativeCoord[1]:
                    R = relativeCoord
            elif relativeCoord[0] < 0:
                if len(L) == 0:
                    L = relativeCoord
                elif L[0]+L[1] > relativeCoord[0]+relativeCoord[1]:
                    L = relativeCoord
            if relativeCoord[0] > 0 and not R:
                R = True
            elif relativeCoord[0] < 0 and not L:
                L = True
        else:
            gradient = relativeCoord[1]/relativeCoord[0]
            if relativeCoord[0] > 0 and relativeCoord[1] > 0:
                if gradient in QPP.keys():
                    if QPP[gradient][0] + QPP[gradient][1] > relativeCoord[0] + relativeCoord[1]:
                        QPP[gradient] = relativeCoord
                else:
                    QPP[gradient] = relativeCoord
            elif relativeCoord[0] > 0 and relativeCoord[1] < 0:
                if gradient in QPN.keys():
                    if QPN[gradient][0] + QPN[gradient][1] > relativeCoord[0] + relativeCoord[1]:
                        QPN[gradient] = relativeCoord
                else:
                    QPN[gradient] = relativeCoord
            if relativeCoord[0] < 0 and relativeCoord[1] > 0:
                if gradient in QNP.keys():
                    if QNP[gradient][0] + QNP[gradient][1] > relativeCoord[0] + relativeCoord[1]:
                        QNP[gradient] = relativeCoord
                else:
                    QNP[gradient] = relativeCoord
            if relativeCoord[0] < 0 and relativeCoord[1] < 0:
                if gradient in QNN.keys():
                    if QNN[gradient][0] + QNN[gradient][1] > relativeCoord[0] + relativeCoord[1]:
                        QNN[gradient] = relativeCoord
                else:
                    QNN[gradient] = relativeCoord
    if U != []:
        relativeList.append(U)
    for key in sorted(QPP, reverse=True):
        relativeList.append(QPP[key])
    if R != []:
        relativeList.append(R)
    for key in sorted(QPN, reverse=True):
        relativeList.append(QPN[key])
    if D!= []:
        relativeList.append(D)
    for key in sorted(QNN, reverse=True):
        relativeList.append(QNN[key])
    if L != []:
        relativeList.append(L)
    for key in sorted(QNP, reverse=True):
        relativeList.append(QNP[key])
    print("Asteroid 200 at " + str(makeNormal(origin, relativeList[199])[0]*100+makeNormal(origin, relativeList[199])[1]))

def makeNormal(origin, relative):
    return [origin[0]+relative[0], origin[1]-relative[1]]

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
orderAsteroidsByGradient(baseLocation, asteroids)

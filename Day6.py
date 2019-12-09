inputString = open("Day6Input.txt").read().splitlines()
orbitMap = {"COM": [0, ""]}

def makeOrbitMap():
    directOrbit = 0
    indirectOrbit = 0
    while len(inputString) > 0:
        for orbit in inputString:
            orbitPair = orbit.split(")")
            if orbitPair[0] in orbitMap:
                orbitMap[orbitPair[1]] = [orbitMap[orbitPair[0]][0] + 1, orbitPair[0]]
                directOrbit += 1
                indirectOrbit += orbitMap[orbitPair[0]][0]
                inputString.remove(orbit)
    print(directOrbit+indirectOrbit)

def findMinJumps(start, end):
    visited = {start}
    adjacents = set()
    rounds = 0
    potentials = getAdjacents(start)
    while orbitMap[end][1] not in potentials:
        for potential in potentials:
            if potential != "":
                adjacents = adjacents | getAdjacents(potential)
                visited.add(potential)
        potentials = adjacents - visited
        rounds += 1
    print(rounds)

def getAdjacents(orbitalBody):
    potentials = set()
    for orbit in orbitMap.items():
        if orbit[1][1] == orbitalBody:
            potentials.add(orbit[0])
    potentials.add(orbitMap[orbitalBody][1])
    return potentials

makeOrbitMap()
findMinJumps("YOU", "SAN")

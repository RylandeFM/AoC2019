inputString = open("Day24Input.txt").read().splitlines()
#inputString = ['....#','#..#.','#..##','..#..','#....']
fieldsFound = set()


def translateFieldToBinary(field):
    binaryString = ""
    for row in field:
        for tile in row:
            if tile == "#":
                binaryString += "1"
            else:
                binaryString += "0"
    return binaryString[::-1]  # Reverse binary string because we build the string left to right


def updateField(field):
    newField = []
    curRow = 0
    for row in field:
        curPos = 0
        rowString = ""
        for tile in row:
            countBugs = 0
            if curPos > 0:
                countBugs += 1 if field[curRow][curPos - 1] == "#" else 0
            if curRow > 0:
                countBugs += 1 if field[curRow - 1][curPos] == "#" else 0
            if curPos < 4:
                countBugs += 1 if field[curRow][curPos + 1] == "#" else 0
            if curRow < 4:
                countBugs += 1 if field[curRow + 1][curPos] == "#" else 0

            if tile == "#":
                rowString += "#" if countBugs == 1 else "."
            else:  # Tile is .
                rowString += "#" if countBugs == 1 or countBugs == 2 else "."
            curPos += 1
        newField.append(rowString)
        curRow += 1

    return newField


def partOne():
    fieldsFound.add(translateFieldToBinary(inputString))
    newField = updateField(inputString)
    binary = translateFieldToBinary(newField)
    while binary not in fieldsFound:
        fieldsFound.add(binary)
        newField = updateField(newField)
        binary = translateFieldToBinary(newField)
    print(int(binary, 2))

partOne()

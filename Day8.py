inputString = open("Day8Input.txt").readline()

layers = []
def createLayers(width, height):
    currentPointer = 0
    for layerNumber in range(int((len(inputString)/width/height))):
        layer = []
        for row in range(height):
            layer.append(inputString[currentPointer:currentPointer+width])
            currentPointer += width
        layers.append(layer)

def partOne():
    minZeros = 999999
    maxOnes = 0
    maxTwos = 0
    for layer in layers:
        countZeros = 0
        countOnes = 0
        countTwos = 0
        for row in layer:
            countZeros += row.count('0')
            countOnes += row.count('1')
            countTwos += row.count('2')
        if countZeros < minZeros:
            minZeros = countZeros
            maxOnes = countOnes
            maxTwos = countTwos
    print(maxOnes*maxTwos)

def partTwo(width, height):
    image = []
    for row in range(height):
        imageRow = ""
        for index in range(width):
            currentLayer = 0
            while layers[currentLayer][row][index] == '2' and currentLayer < (width*height)-1:
                currentLayer += 1
            if layers[currentLayer][row][index] == '1':
                imageRow += 'W'
            else:
                imageRow += ' '
        image.append(imageRow)
    for imageRow in image:
        print(imageRow)

createLayers(25, 6)
partOne()
partTwo(25, 6)

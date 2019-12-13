import random

def shiftChar(c, shift):
    return chr(((ord(c)-65+shift) % 26)+65)

def firstEncode(input, shift, start, length):
    index = 0
    position = 1
    encoded = {}

    for c in input:
        encoded[index+start] = shiftChar(c, shift)
        if position % 2 == 0:
            index += 1
        else:
            index += 3
        position += 1

    outputString = ""
    for i in range(1,length):
        if i in encoded.keys():
            outputString += encoded[i]
        else:
            outputString += chr(random.randrange(65,65+26))
    print(outputString)

def secondEncode(input, number, shift):
    position = 1
    encoded = {}
    encodeString = ""
    for c in input:
        encoded[((position*number)%len(input))+1] = shiftChar(c, shift)
        position += 1
    for i in sorted(encoded):
        encodeString += encoded[i]
    print(encodeString)

def thirdEncode(input, number):
    position = 1
    encodeString = ""
    for c in input:
        if position*number % 2 == 0:
            encodeString += shiftChar(c, position*number)
        else:
            encodeString += shiftChar(c, -position*number)
        position += 1
    print(encodeString)

def fourthEncode(input, n1, n2):
    position = 1
    shiftString = ""
    encodeString = ""
    shiftStringCheat = []
    for c in input:
        shiftStringCheat.append((position*position+(n1*position)+n2) % 26)
        shiftString += chr(((position*position+(n1*position)+n2) % 26)+64)
        encodeString += shiftChar(c, ord(shiftString[position-1])-64)
        position += 1
    print(encodeString)

firstEncode("PIANO", 5, 3, 14)
secondEncode("BADKAMER", 5, -4)
thirdEncode("KEUKENLA", 3)
fourthEncode("SLAAPKAMER", 4, 4)

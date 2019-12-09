startNum = 367479
endNum = 893698

def checkNumber(number, additional):
    hasDouble = False
    noError = True
    for i in range(1, 6):
        doubleFound = number.count(number[i]) == 2 if additional else True
        if number[i-1] == number[i] and doubleFound:
            hasDouble = True
        if int(number[i]) < int(number[i-1]):
            noError = False
    return hasDouble and noError

def checkNumbers(doublesRequired):
    counter = 0
    for number in range(startNum, endNum):
        if checkNumber(str(number), doublesRequired):
            counter += 1
    print(counter)

checkNumbers(False)
checkNumbers(True)

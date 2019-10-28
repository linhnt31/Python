""" Link: https://app.codesignal.com/tournaments/LJmRXKvn6JbD8JQGG """

#A
def minMaxDifference(inputArray):

    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMaximum]:
            indexOfMaximum = i
    return abs(inputArray[indexOfMinimum] - inputArray[indexOfMaximum])

#B
def regularBracketSequence1(sequence):

    balance = 0
    for i in range(len(sequence)):
        if sequence[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    if balance != 0:
        return False
    return True

#C
def pepEight(line):
    return line <= 79


#D
def firstDigit(inputString):
    for x in inputString:
        if '0' <= x <= '9':
            return x

#E
def chessKnight(cell):
    X = ord(cell[0]) - 96
    Y = ord(cell[1]) - 48
    indexX = [1, -1, 2, -2]
    indexY = [2, -2, 1, -1]
    
    res = 0
    for i in range(len(indexX)):
        for j in range(len(indexY)):
            if 1<= (X + indexX[i]) <= 8 and 1 <= (Y + indexY[j]) <= 8:
                res += 1
                
    return res // 2


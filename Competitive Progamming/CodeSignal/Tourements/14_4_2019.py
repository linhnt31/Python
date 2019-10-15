# https://app.codesignal.com/tournaments/WX7e5mxzqNA5LYHg4/D

def axisAlignedBoundingBox(x, y):

    max_X, min_X = max(x), min(x)
    max_Y, min_Y = max(y), min(y)
    
    return abs(max_X - min_X) * (max_Y - min_Y)

# https://app.codesignal.com/tournaments/WX7e5mxzqNA5LYHg4/E

def matrixTrace(matrix):
    sum_ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum_ += matrix[i][j]
    return sum_

# https://app.codesignal.com/tournaments/mq4PzeE2ndj9uQfGh/B

def arrayMode(sequence):
    count = []
    answer = 0

    for i in range(1000):
        count.append(0)
    for i in range(len(sequence)):
        count[sequence[i] - 1] += 1
        if count[sequence[i] - 1] > count[answer]:
            answer = sequence[i] - 1
    return answer + 1

# https://app.codesignal.com/tournaments/mq4PzeE2ndj9uQfGh/D

def arrayMaximalDifference(inputArray):

    max_ = -float('inf')
    
    for i in range(0, len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            tmp = abs(inputArray[i] -  inputArray[j])
            if tmp > max_:
                max_ = tmp
    return max_

# https://app.codesignal.com/tournaments/mq4PzeE2ndj9uQfGh/E

def insideCircle(a, b, radius):

    return (a[0] - b[0]) ** 2 +  (a[1] - b[1]) ** 2  <= radius * radius
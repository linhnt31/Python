'''
- Link: https://app.codesignal.com/tournaments/owHPwiXEH2FXuLwAa
'''

#
def sumOfMultiples(n, k):

    result = 0

    for i in range(1, n + 1):
        if i % k == 0:
            result += i
    return result


#
def bfsComponentSize(matrix):
    visited = [False for i in range(len(matrix))]
    queue = []
    componentSize = 0

    visited[1] = True
    queue.append(1)
    while len(queue) > 0:
        currentVertex = queue.pop()
        visited[currentVertex] = True
        componentSize += 1
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                queue.append(nextVertex)

    return componentSize

#
def sortByLength(inputArray):
    return sorted(inputArray, key = len)


#
def knapsackLight2(weight1, weight2, maxW):
    if weight1 > maxW and weight2 <= maxW:
        return 'second'
    elif weight1 <= maxW and weight2 > maxW:
        return 'first'
    elif weight1 + weight2 <= maxW:
        return 'both'
    elif weight1 <= maxW and weight2 <= maxW:
        return 'either'
    return 'none'


#
def minimalMultiple(divisor, lowerBound):
    while lowerBound % divisor != 0:
        lowerBound += 1
    return lowerBound

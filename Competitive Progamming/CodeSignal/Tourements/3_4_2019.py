'''
- Link: https://app.codesignal.com/tournaments/J9xfqqC9H3QCqL8oc
'''

#
def reverseToSort(inputArray):

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray) + 1):
            left = inputArray[:i]
            middle = inputArray[i:j]
            middle.reverse()
            right = inputArray[j:]
            result = []
            correct = True

            result = left + middle + right

            for k in range(1, len(result)):
                if result[k - 1] >= result[k]:
                    correct = False
                    break
            if correct:
                return True
    return False

#
def equidistantTriples(coordinates):

    ans = 0
    for i in range(1, len(coordinates)):
        left = i - 1
        right = i + 1
        while left >= 0 and right < len(coordinates):
            distL = -coordinates[left] + coordinates[i]
            distR = coordinates[right] - coordinates[i]
            if distL == distR:
                ans += 1
                left -= 1
                right += 1
            elif distL < distR:
                left -= 1
            else:
                right += 1

    return ans

#
def squareDigitsSequence(a0):

    seq = [a0]
    while seq[-1] not in seq[:-1]:
        seq.append(sum(int(i) ** 2 for i in str(seq[-1])))
    return len(seq)
#
def chessKnightMoves(cell):

    x, y = ord(cell[0]) - ord('a'), int(cell[1]) - 1
    # count = 0
    # for i in range(-2, 3):
    #     for j in range(-2, 3):
    #         if abs(i * j) == 2 and 0 <= x + i < 8 and 0 <= y + j < 8:
    #             count += 1
    # return count  
    
    #Using list comprehension 
    return sum(abs(dx * dy) == 2 and 0 <= x + dx < 8 and 0 <= y + dy < 8 \
               for dx in range(-2, 3) for dy in range(-2, 3))
    
    
#
def kStepMaximization(n, k):
    z = set()
    z.add(n)
    for _ in range(k):
        t = set(z)
        for a in z:
            t.add(a + 1)
            t.add(2 * a)
            b = rotate(a)
            if b >= 0:
                t.add(b)
        z = t
    return max(z)

def rotate(a):
    r = 0
    while a > 0:
        d = a % 10
        if d == 3 or d == 4 or d == 7: return -1
        if d == 6:
            d = 9
        else:
            if d == 9:
                d = 6
        r = r * 10 + d
        a //= 10
    return r

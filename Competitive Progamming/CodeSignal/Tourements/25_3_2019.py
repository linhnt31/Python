'''
- Link: https://app.codesignal.com/tournaments/B42M6nJN3naM87RGo
- Link: https://app.codesignal.com/tournaments/G5Nhbb3tAQQaEkJNs
- Link: https://app.codesignal.com/tournaments/rb6h52W8LdcpdCiFA
'''

#
def fractionReducing(fraction):

    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    commonDivisor = gcd(fraction[0], fraction[1])
    fraction[0] /= commonDivisor
    fraction[0] /= commonDivisor

    return fraction

#
def differentValues(a, d):

    best = -1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = abs(a[i] - a[j])
            if diff <= d and best < diff:
                best = diff

    return best

#
def arithmeticProgression(element1, element2, n):
    diff = element2 - element1
    res = element2
    for _ in range(2, n):
        res += diff
    return res
#
def kthDigit(n, k):
    tmp = str(n)
    if k <= 0 or k > len(tmp):
        return -1
    return int(tmp[k- 1])

#
def candies(n, m):
    if n > m:
        return 0
    return m - m % n

#
def pepEight2(line):
    l = len(line)
    return l >= 79

#
def uniqueDigitProducts(a):
    res = []
    for x in a:
        res.append(product(x))
    return len(set(res))

def product(n):
    res = 1
    while n > 0 :
        res *= n % 10
        n //= 10
    return res 
#
def firstMultiple2(divisors, start):
    while True:
        for x in divisors:
            if start % x == 0:
                return start
        start +=1

#
def stringsCrossover(inputArray, result):

    answer = 0

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            correct = True
            for k in range(len(result)):
                if (result[k] != inputArray[i][k]
                  and result[k] != inputArray[j][k]):
                    correct = False
                    break
            if correct:
                answer += 1
    return answer

#
def generatePalindromes(charactersSet):

    result = []

    N = len(charactersSet)
    palindrome = [0] * N
    letterCnt = [0] * 26

    for i in range(N):
        letterCnt[ord(charactersSet[i]) - ord('a')] += 1
    if N % 2 == 1:
        for i in range(26):
            if letterCnt[i] % 2 == 1:
                letterCnt[i] -= 1
                palindrome[N // 2] = chr(ord('a') + i)
                break

    def generate(idx):
        if idx >= N // 2:
            result.append(''.join(palindrome))
            return
        for i in range(26):
            if letterCnt[i] >= 2:
                letterCnt[i] -= 2
                palindrome[idx] = chr(ord('a') + i)
                palindrome[N - idx - 1] = chr(ord('a') + i)
                generate(idx + 1)
                letterCnt[i] += 2

    generate(1)
    return result

#
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

# So long --> need to optimize solution 
def insertDashes(inputString):
   res = []
   for i in range(len(inputString) - 1):
      if inputString[i + 1] != ' ' and inputString[i] != ' ':
         res.append(inputString[i] + '-')
      else:
         res.append(inputString[i])
   res.append(inputString[-1])
   return "".join(res)

def insertDashesOtimized(s):
    return ' '.join('-'.join(list(u)) for u in s.split())


#
def oddNumbersBeforeZero(sequence):
    count = 0
    for x in sequence:
        if x == 0:
            return count
        if x % 2 != 0:
            count += 1

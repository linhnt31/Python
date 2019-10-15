"""
-Link: https://app.codesignal.com/tournaments/38HbY4SpdgtLTw7aY
"""

#
def rightmostRoundNumber(inputArray):

    ans = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            ans = i

    return ans

#
def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i])
        if ord('A') <= code and code <= ord('Z'):
            code += ord('a') - ord('A')
        if ord('a') <= code <= ord('z'):
            found[code - ord('a')] = True

    for i in range(26):
        if not found[i]:
            result = False

    return result

#
def replaceAllDigitsRegExp(input):

    res = ''
    for ch in input:
        if ch.isdigit():
            res += '#'
        else:
            res += ch
    return res

#
def removeDuplicateCharacters(str):

    res = ""
    s = set()
    
    for ch in str:
        if ch in s: 
            res= res.replace(ch, '')
        else:
            res += ch
        s.add(ch)
    return res
    
#
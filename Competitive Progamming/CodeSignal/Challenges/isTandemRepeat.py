'''
- Link: https://app.codesignal.com/challenge/b88Cu9b88ymnXxw7h
'''

def isTandemRepeat(inputString):
    len_ = len(inputString)
    if len_ % 2 != 0:
        return False
    return inputString[:len_//2] == inputString[len_//2:]
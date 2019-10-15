'''
- Link: https://app.codesignal.com/challenge/Dp6Yojn6Wfv78yG5A
'''

def nearestRoundNumber(value):
    if value % 10 == 0:
        return value
    return value + 10 - (value % 10)

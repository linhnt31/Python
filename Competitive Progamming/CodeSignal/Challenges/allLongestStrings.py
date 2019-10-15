'''
- Link: https://app.codesignal.com/challenge/yasLrrbACoCsFSPCE
'''

def allLongestStrings(inputArray):
    max_len = -float('inf')
    
    for x in inputArray:
        max_len = max(max_len, len(x))
    
    return [i for i in inputArray if len(x) >= max_len]

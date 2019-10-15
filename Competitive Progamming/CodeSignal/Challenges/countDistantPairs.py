'''
- Link :https://app.codesignal.com/challenge/Npv4LdeuiEZBbw2JF
'''

def countDistantPairs(inputString, distance):
    count = 0
    
    for i in range(0, len(inputString) - distance - 1):
        if inputString[i] == inputString[i + distance + 1]:
            count += 1
    return count

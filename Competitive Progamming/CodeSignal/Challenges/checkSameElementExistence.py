"""
-Link: https://app.codesignal.com/challenge/4uuajLD5XiSsYMzgD
"""

def checkSameElementExistence(arr1, arr2):

    i, j = 0, 0
    
    #Time complexity: O(l1 + l2)
    # l1 and l2 are length of 2 arrays arr1 and arr2
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            return True
    return False
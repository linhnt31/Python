"""
-Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""

def isSubsequence(x, y): # len(x) <= len(y)
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            i += 1
        j += 1
    return i == len(x)

    
def __ord(s):
    res = 0
    for sub in s:
        res += ord(sub)
    return res

#Time complexity: O(n*x)- x is average length of strings in list
#Space complexity: O(k): max_str variable is used
def findLongestWord(s, fruits):
    max_str = ''
    for fruit in fruits:
        if isSubsequence(fruit, s):
            if len(fruit) > len(max_str) or len(fruit) == len(max_str) \
                and __ord(fruit) < __ord(max_str):
                max_str = fruit

    return max_str


if __name__ == "__main__":
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    print(findLongestWord(s, d))
"""
- You must check a string whether Is it a palindrome if we change some characters.
Example: 
str = "Abaab"
output: True --> baaab or BAAAB or ababa or AbabA and so on
"""

def checkPalindrome(string):
    if len(string) <= 1:
        return True

    tmp = list(string)
    res = []
    for x in set(tmp):
        res.append(tmp.count(x))
        
    count_odd = 0
    for x in res:
        if x == 1:
            count_odd += 1
    return count_odd < 2

if __name__ == "__main__":
    string = input('Enter a random string: ')
    print("{} can be a palindrome : {} ".format(string, checkPalindrome(string)))
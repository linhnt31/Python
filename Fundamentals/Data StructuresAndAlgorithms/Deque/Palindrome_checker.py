'''
-Link: http://interactivepython.org/runestone/static/pythonds/BasicDS/PalindromeChecker.html

'''

from pythonds.basic.deque import Deque
from DeQue import Deque


#no standard
def palindrome(string):
    #initialize a obj of class Deque
    deQue = Deque()

    for i in range(len(string) // 2):
        deQue.addRear(string[i])
        deQue.addFront(string[len(string) - i - 1])

    for _ in range(len(string) // 2):
        if deQue.removeFront() != deQue.removeRear():
            return False
    
    return True

#Standard
def pal_checker(string):
    char_deque = Deque()

    for ch in string:
        char_deque.addFront(ch)

    stillEqual = True

    while char_deque.size() > 1 and stillEqual:
        first = char_deque.removeRear()
        last  = char_deque.removeFront()

        if last != first:
            stillEqual = False
    
    return stillEqual


if __name__ == "__main__":
    string = str(input("Enter a random string: "))
    # checker = palindrome(string) #method 1
    checker = pal_checker(string)

    if checker == True:
        print(string + " is palindrome")
    else:
        print(string + " is not palindrome")
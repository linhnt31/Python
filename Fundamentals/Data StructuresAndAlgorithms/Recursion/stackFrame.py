"""
#Referrences:
http://interactivepython.org/runestone/static/pythonds/Recursion/StackFramesImplementingRecursion.html

"""
from pythonds.basic.stack import Stack

def __toStr(n, base):
    convertString = "0123456789ABCDEF"
    res_stack = Stack()

    while n > 0:
        if n < base:
            res_stack.push(convertString[n])
        else:
            res_stack.push(convertString[n % base])

        n //= base
    
    res = []
    while not res_stack.isEmpty():
        res.append(res_stack.pop())
    return "".join(res)

if __name__ == "__main__":
    n = int(input("Enter a random integer: "))
    print("After converting: {}".format(__toStr(n, 16)))
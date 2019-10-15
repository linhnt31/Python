'''
Convert the following values to binary using “divide by 2.” 
Show the stack of remainders.
- 17
- 45
- 96
'''
from Stack import Stack

def convertBinary(n):
    num_stack = Stack()
    res = ''

    while n > 0:
        num_stack.push(n % 2)
        n //= 2
    
    # num_stack.__str__()
    while not num_stack.isEmpty():
        res += str(num_stack.pop())
    
    return res

#main

if __name__ == "__main__":
    n = int(input('Enter a random interger: '))
    print('After convert : {}'.format(convertBinary(n)))
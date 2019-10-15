'''
- Practice : infix to postfix
'''

from Stack import Stack
import string

def infixToPostfix(infix):

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    tokens = infix.split()
    postfixList = []
    opStack = Stack()

    for token in tokens:
        if token in string.ascii_uppercase or token in string.digits:
            postfixList.append(token)
        
        elif token == '(':
            opStack.push(token)

        elif token == ')':

            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        
        else:
            while not opStack.isEmpty() and \
                prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)

if __name__ == "__main__":
    while True: 
        infix = str(input('Enter a random string: '))
        print('postfix: ', infixToPostfix(infix))
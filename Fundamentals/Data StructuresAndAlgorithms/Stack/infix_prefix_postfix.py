'''
- infix: the operator is in between the two operands
    - ex: A + B
- prefix: Move operator before 2 operands
    - ex: +AB
- postfix: Move the operator to the end
    - ex: AB+

Infix Expression	Prefix Expression	Postfix Expression

A + B * C + D	    + + A * B C D	    A B C * + D +
(A + B) * (C + D)	* + A B + C D	    A B + C D + *
A * B + C * D	    + * A B * C D	    A B * C D * +
A + B + C + D	    + + + A B C D	    A B + C + D +
'''

""" Infix to Postfix """

from Stack import Stack
import string

def infixToPostfix(infix):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infix.split()

    for token in tokenList:
        if token in string.ascii_uppercase or token in string.digits:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()

            while topToken != '(':
                postfixList.append(topToken)
                # if not opStack.isEmpty():
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) \
                and (prec[opStack.peek()] > prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

if __name__ == "__main__":
    while True: 
        infix = str(input('Enter a infix expression: '))
        print('Infix: ', infix)
        print('Result: ', infixToPostfix(infix))



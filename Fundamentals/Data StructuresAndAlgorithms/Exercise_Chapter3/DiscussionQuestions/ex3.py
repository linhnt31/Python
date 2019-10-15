'''
- Convert the below infix expressions to postfix (use full parentheses).
. (A+B)*(C+D)*(E+F)
.  A+((B+C)*(D+E))
.  A*B*C*D+E+F
'''

from pythonds.basic.stack import Stack
import string
import pdb

def _infixToPostfix(infix):
    prec = {}

    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    postfixList = []
    op_stack = Stack()

    tokensList = infix.split()
    for token in tokensList:
        if token in string.ascii_uppercase or token in string.digits:
            postfixList.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while op_stack.peek() != '(':
                postfixList.append(op_stack.pop())
            op_stack.pop()
        else:
            while not op_stack.isEmpty() \
                and prec[op_stack.peek()] >= prec[token]:
                postfixList.append(op_stack.pop())
            else:
               op_stack.push(token)

    while not op_stack.isEmpty():
        postfixList.append(op_stack.pop())
     
    return " ".join(postfixList)

#main
if __name__ == "__main__":
    infix = str(input('Enter a random string: '))
    postfix = _infixToPostfix(infix)

    print('After converting infix to postfix: {}'.format(postfix))
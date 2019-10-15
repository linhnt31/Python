'''
-Description: 
Convert the following infix expressions to prefix (use full parentheses):
+)  (A+B)*(C+D)*(E+F)
+)  A+((B+C)*(D+E))
+)  A*B*C*D+E+F

----> Key: this is a reverse math of converting infix to postfix
'''

import string
from pythonds.basic.stack import Stack

def infixToPostfix(infix):
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
        #To avoid exception in final else 
        #pre[' '] will not find
        if token in string.whitespace:
            continue
        elif token in string.ascii_uppercase or token in string.digits:
            postfixList.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while op_stack.peek() != '(':
                postfixList.append(op_stack.pop())
            op_stack.pop()
        else:
            while not op_stack.isEmpty() \
                and prec[op_stack.peek()] > prec[token]:
                postfixList.append(op_stack.pop())
            else:
               op_stack.push(token)

    while not op_stack.isEmpty():
        postfixList.append(op_stack.pop())
     
    return " ".join(postfixList)


#Time complexity : O(n)
#Space complexity: 
def infixToPrefix(infix):
    _infix = reversing(infix)
    prefixString = infixToPostfix(_infix)

    return prefixString[:: -1]


def reversing(infix):
    resverse_string = infix[::-1]
    res = []
    for x in resverse_string:
        if x == ')':
            res.append('(')
        elif x == '(':
            res.append(')')
        else:
            res.append(x)
    
    return " ".join(res)


if __name__ == "__main__":
    infix = str(input('Enter a random string: '))
    print('After converting infix to prefix: {}'.format(infixToPrefix(infix)))
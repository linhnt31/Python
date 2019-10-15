from Stack import Stack
import string

def postFixCaculate(postFix):

    operandStack = Stack()
    tokenList = postFix.split()

    for token in tokenList:
        if token in string.digits:
            operandStack.push(int(token))

        else:
            tmp_res = doMath(token, operandStack.pop(), operandStack.pop())
            operandStack.push(tmp_res)
    
    return operandStack.pop()

def doMath(operator, firstTop, secondTop):
    if operator == '+':
        return secondTop + firstTop
    elif operator == '-':
        return secondTop - firstTop
    elif operator == '*':
        return secondTop * firstTop
    elif operator == '/':
        return secondTop / firstTop


if __name__ == "__main__":
    postfix = str(input('Enter a postfix string: '))
    print(postFixCaculate(postfix))
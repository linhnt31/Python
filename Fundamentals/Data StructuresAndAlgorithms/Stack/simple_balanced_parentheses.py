from Stack import Stack

def checkBalanced(symbolString):
    s = Stack()
    for sub_str in symbolString:
        if sub_str == '(':
            s.push(sub_str)
        if sub_str == ')':
            if s.isEmpty():
                return 'Unbalanced'
            s.pop()
    if s.isEmpty():
        return 'Balanced'
    return 'Unbalanced'

if __name__ == "__main__":
    symbolString = str(input('Enter a random string: '))

    print(checkBalanced(symbolString))
    
from Stack import Stack


def parChecker(symbolString):
    s = Stack()
    opens = '([{'
    closes = ')]}'

    for sub_str in symbolString:
        if sub_str in opens:
            s.push(sub_str)

        #When we enter a random input , string can store white space
        # So we should not use else
        elif sub_str in closes:
            ''' Optimization '''
            if s.isEmpty():
                return 'Unbalanced'
            else:
                if opens.index(s.peek()) != closes.index(sub_str):
                    return 'Unbalanced'
                s.pop()

    if s.isEmpty():
        return 'Balanced'
    return 'Unbalanced'

if __name__ == "__main__":
    symbolString = str(input('Enter a random string: '))
    print(parChecker(symbolString))

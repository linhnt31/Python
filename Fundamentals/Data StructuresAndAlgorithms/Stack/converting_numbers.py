from Stack import Stack

def baseConvert(decNumber, base):
    digits = '0123456789ABCDEF'

    remStack = Stack()

    while decNumber > 0:
        remStack.push(decNumber % base)
        decNumber //= base
    
    res = []
    while not remStack.isEmpty():
        res.append(digits[remStack.pop()])
    
    return ''.join(res)

if __name__ == "__main__":
    print(baseConvert(15, 16))
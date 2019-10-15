import string

def removeTrash(inputString):
    res = []
    for ch in inputString:
        if ch not in string.punctuation and ch != " ":
            res.append(ch)
    return "".join(res)

def __palinDrome(inputString):
    length = len(inputString)

    if length <= 1:
        return True
    if inputString[0] == inputString[length - 1]:
        return __palinDrome(inputString[1 : length - 1])
    
    return False

if __name__ == "__main__":
    input = input("Enter a random string: ")
    inputString = removeTrash(input)
    print(inputString)

    if __palinDrome(inputString):
        print("{} is palindrome".format(inputString))
    else:
        print("{} is not palindrome".format(inputString))
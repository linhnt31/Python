import string

#Problem 1: converting integer to string

def __convertInt(n, base):
    convertString = "0123456789ABCDEF"

    #base case
    if n < base:
        return convertString[n]
    return convertString[n % base] + __convertInt(n // base, base)


#Problem 2: reversing a string

def __reverString(inputString):
    length = len(inputString)

    if length <= 1:
        return inputString
    return inputString[length - 1] + __reverString(inputString[0: length - 1])


#Problem 3: palindrome 

def __checkPalindrome(inputString):
    length = len(inputString)

    #base case
    if len(inputString) <= 1:
        return True
    if inputString[0] == inputString[length - 1]:
        return __checkPalindrome(inputString[1 : length - 1])

    return False
    

def __handleString(inputString):
    res = []
    for ch in inputString:
        if ch not in string.punctuation and ch != " ":
            res.append(ch)
    return "".join(res)
        

#main
if __name__ == "__main__":
    # n = int(input("Enter a random string: "))
    # print("After converting to base: {}".format(__convertInt(n, 2)))

    # inputString = input("Enter a random string: ")
    # print("After reversing: {}".format(__reverString(inputString)))

    inputString = input("Enter a random string: ").lower()
    inputString = __handleString(inputString)
    
    check = __checkPalindrome(inputString)
    if check:
        print("{} is palindrome ".format(inputString))
    else:
        print("{} is not palindrome".format(inputString))

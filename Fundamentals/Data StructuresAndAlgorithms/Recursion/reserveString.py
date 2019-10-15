def reverse(inputString):
    length = len(inputString)
    if length == 0:
        return inputString
    return reverse(inputString[1:]) + inputString[0]

if __name__ == "__main__":
    print(reverse('hello'))
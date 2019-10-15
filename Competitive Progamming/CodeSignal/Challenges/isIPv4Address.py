"""
- Link: https://app.codesignal.com/tournaments/3zaRKaXy9RDuDPntf/A/solutions
"""

def _IPv4Address(inputString):

    current_number = 0
    empty_field = True
    count_dot = 0

    for i in range(len(inputString)):
        if inputString[i] == '.':
            if empty_field:
                return False
            count_dot += 1
            empty_field = True
            current_number = 0
        else:
            digit = ord(inputString[i]) - ord('0')
            if digit < 0 or digit > 9:
                return False
            empty_field = False
            current_number = current_number * 10 + digit

            if current_number < 0 or current_number > 255:
                return False
    return count_dot == 3
    

if __name__ == "__main__":
    inputString = input('Enter a string: ')
    check_ip = _IPv4Address(inputString)

    print('{} is {}'.format(inputString, check_ip))
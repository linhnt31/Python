"""
- Link: https://app.codesignal.com/tournaments/j3MTtK6Gnc3tp7dui/B
"""

def factorSum_(n):
    next_value = n
    current_value = 0
    previous_value = 0

    while next_value != previous_value:
        previous_value = next_value
        current_value = next_value
        next_value = 0
        divisors = 2

        while divisors * divisors <= current_value:
            if current_value % divisors == 0:
                next_value += divisors
                current_value //= divisors
            else:
                divisors += 1
        next_value += current_value

    return next_value

if __name__ == "__main__":
    n = int(input('Enter a random number: '))
    print('factor of sum is {}'.format(factorSum_(n)))
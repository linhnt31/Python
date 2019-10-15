def f(x):
    return 9 - x * (x - 10)

def f_prime(x):
    return -2 * x + 10

guess = 11 

for val in range(1, 10):
    next_guess = guess - f(guess)/ f_prime(guess)
    print(next_guess)
    guess = next_guess


print(f(guess))
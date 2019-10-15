#Python3 code to demonstrate 'yield keyword'

#generator to print even numbers

def print_even(lst):
    for i in lst:
        if i  % 2 == 0:
            yield i

# lst = [1, 2, 3, 4, 5, 6, 7]

# for j in print_even(lst):
#     print(j, end=" ")

def next_square():
    i = 1

    while True:
        yield i * i
        i += 1

# for num in next_square():
#     if num > 100:
#         break
#     print(num)

''' 
- Handling the last amount of data and searching 
'''


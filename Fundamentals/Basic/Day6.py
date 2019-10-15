'''
- try... except, module python, function, create virtuallenv
'''

# try:
#     a, b = 1, 0
#     c = a / b
#     d = 10 + ""
# except ZeroDivisionError as e:
#     print('Division by zero')
#     print(e)
# except TypeError:
#     print('Must be str not int')
# except Exception as e:
#     print('finnaly')
#     print(e)
# finally:
#     print('End process')


# try:
#     a, b = 1, 0
#     c = a / b
# except Exception:
#     print('')

''' Different between if/else and try...except '''

''' Race-condition '''

#Multi-thread / multi-process


''' Module
- standard lib: string, math
- lib installed by using pip: pip install packages_name
- python module: python file .py
'''

'''Function '''

# Naming: 
# snake_case
# camelCase



"""Lambda"""

# foo = lambda x : x * 2
# add = lambda x, y, z : x + y + z
# print(add(1, 2, 3))


# import string

# letters = string.ascii_letters

# def len_of_letter(letter):
#     len_lt = 0
#     for sub_letter in letter:
#         len_lt += letters.index(sub_letter) + 1
#     return len_lt

# print(len_of_letter('python'))

# def add(a, b=1, c=7):
#     return b + a + c
# print(add(1))



""" Mandatory argument and optional argument """
""" Positional argument : no need assignment value, must be stand in front of """ 


# x = 1

# def add():
#     global x #global
#     x += 1 #local
#     print(x)

# add()

''' Nested function '''

# def foo(a, b, c):

#     def bar(a, b, c):
#         return sum([a, b, c])

#     return bar(a, b, c)

# print(foo(1, 2, 3))


from pprint import pprint #pretty print


'''Underscore
- _sum : private ---> 
''' 

""" Dictionary unpacking """ 








""" Virtualenv : create a vitural environment """ 
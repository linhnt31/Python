"""unpacking""" 
# def foo(a, b, c, d):
#     print(a, b, c, d)

# my_lst = [1, 2, 3, 4]

# #Unpacking list into 4 arguments
# foo(*my_lst)


# lst = [i for i in range(3, 5)]
# print(lst)


"""Packing"""

# def mySum(*args):
#     sum_ = 0

#     for i in range(0, len(args)):
#         sum_ += args[i]
    
#     return sum_

# print(mySum(1, 2, 3 , 4))


"""packing and unpacking """

# def fun1(a, b, c):
#     print(a, b, c)

# def fun2(*args):
#     #Convert args tuple to a list so we can modify it
#     args = list(args)

#     #Modifying args
#     args[0] = 'Linh'
#     args[1] = 'Nguyen'

#     #Unpacking args and calling fun1()
#     # fun1(*args)

# fun2('Hello', 'my', 'brother')


""" ** operator is used for dictionaries """

# def fun(a, b, c):
#     print(a, b, c)

# d = {
#     'a' : 2,
#     'b' : 3,
#     'c' : 4
# }

# #A call with unpacking of dictionary
# fun(**d)

def fun(**kwargs):

    print(type(kwargs))

    for key in kwargs:
        print('{} = {}'.format(key, kwargs[key]))

fun(name='Linh', id='317',language='Python')


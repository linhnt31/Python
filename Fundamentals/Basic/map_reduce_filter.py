'''
- Link exercises: https://app.codesignal.com/arcade/python-arcade/caravan-of-collections
'''
'''
- map(func , inp_list)
'''

# items = [1, 2, 3, 4, 5]
# squared = list((map(lambda x: x ** 2, items)))

# print(squared)


'''
- filter(func, inp_list)
'''

# numb_list = range(-4, 4)

# def lon_hon_zero(numb):
#     if numb > 0 :
#         return True
#     return False
# # more_than_zero = list(filter(lambda x: x > 0, numb_list))
# more_than_zero = list(filter(lon_hon_zero, numb_list))
# print(more_than_zero)

'''
- reduce(func(arg1, arg2) , inp_list)
- Must import functools
'''
import functools
from functools import reduce
# data = [1, 2, 3, 4]

# def sum_of_list(sum_, numb):
#     return sum_ + numb

# res = reduce(sum_of_list, data)
# res_ = reduce(lambda x, y: x + y, data)
# print(res)
# print(res_)

'''
Some exercises on CodeSignal
'''

#
def chessTeams(smarties, cleveries):
    return [[a,b] for a,b in zip(smarties, cleveries)]

#
def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))

#
def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))

#
def createHistogram(ch, assignments):
    return list(map(lambda x : ch * x, assignments))

#
from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda x, y : (x*y) // gcd(x,y), denominators)

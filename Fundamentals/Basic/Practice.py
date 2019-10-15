'''
- Map, reduce, filter
'''
from functools import reduce
lst = [1, 3, 9, 12, 17, 4]
res_map = list(map(lambda x : x ** 3, lst))
print(res_map)

res_filter = list(filter(lambda x: x % 2 == 0, lst))
print(res_filter)

res_reduce = reduce(lambda x, y: x + y, lst)
print(res_reduce)
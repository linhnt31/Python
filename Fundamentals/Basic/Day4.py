""" Tuple is immutable ----     mutable: list, dict , set """


# demo_tuple = ()  #paranthesis
# tup = (1, 2, 3, 4, 5)
# print(type(tup), tup)

# demo2_tuple = (1, ) #create a element

# print(demo2_tuple)
# print(type(demo2_tuple))

# tup = ([1, 2, 3], 5.9, 'Linh', True, 2 + 4j, (1, 3))
# print(tup, type(tup))

# tup1 = (1, 2, 3)
# print(tup1[2])

#tuple is iterable

# tup = (1, 2, 3, 1, 5, 10, 12)
# print(tup.count(1))
# print("Index: {}".format(tup.index(2)))


# ''' '''
# a, b = 1, 2 #unpacking
# print(a, b)

# t = 1, 2, 3 #packing  <--->  t = (1, 2, 3)
# print(type(t))

# x, y, z = t #unpacking
# print(x, y, z)

''' generator '''  #convenient for data science
# tup = (i * 2 for i in range(0, 10) )  # generator
# print(tup)


# for numb in tup:
#     print(numb)




"""
la = [ 1, 2, 3]
print(la)

la2 = [1, 2, 10.05, True]
print("Len of list {}".format(len(la2)))
print("type of list {}".format(type(la2)))

list1 = [[1,2,3], True, False]
print(list1)
print()

"""



"""Indexing"""
# nested_list = [1, 2, 3, [1,2,3]]

# la = list(range(10, 43))
# print(la)
# print("value of last element {}".format(la[-1]))

# test = list("python")
# print(test[-6])




"""Slicing: """

# ls = list("python")
# print(ls[:])
# print(ls[:3])
# print(ls[0::2])

# #reserve string
# print(ls[::-1])
# print(ls[::-1][::-1])


"""Matrix"""

# matrix = [[1,2,3],[4,3,2],[7,8,9]]
# print(matrix)
# print(matrix[1][1])
# print(len(matrix))


"""Data science : numpy.org"""

"""range(start: stop : step) : value of indices must be integer """
# print(list(range(10)))
# print(list(range(2, 5)))
# print(list(range(-10, -1)))
# print(list(range(10, 50, 3)))
# print(list(range(1.0, 10.0)))

"""-------------------List method-------------------------"""

'''1..append(obj) : only 1 agurment ---> return None'''
# la = []
# la.append(1)
# print(la)
# la.append([1, 2, 3])
# la.append(True)
# la.append(None)
# print(len(la))
# print(la)

"""Use method id() to find memory address"""

''' 2..clear()  

    3..copy(): comprise  + shallow copy : access 1 level of list 
                                    + deep copy : access levels

    4..count():

    5..extend(): != append()

    6..index():

    7..insert(pos, Obj):

    8.pop():


    '''
            #id and copy()
# la = [1, 2, 3]
# print("before clear: ")
# lb = la.copy()
# la[2] = 999
# print("Address of la: ")
# print(id(la))
# print("Address of lb: ")
# print(id(lb))

            #  count  
# la = [1, 2, 3, [4, 5, 6]]
# la = list("PythonPythonJava")
# rest = la.append('100')
# print(len(la))
# print("Count: {}".format(la.count('a')))
# print(rest)

            #extend != append
# la = [1, 2, 3]
# la.extend([4,5,6])
# print(la)
# la.extend([4,5,6])
# print(la)
# print(la.index(1))
# la.remove(4)
# print(la)

# la = list("Linh")
# la.reverse()
# print(la)

# lb = list("python")
# lb.sort()
# print(lb)

# print(dir(la))



la = list(range(0,1000))

lb = la[::3]
lc = la[::5]
sum_of_15 = list(range(0,1000,15))
print(sum(lb)+sum(lc)- sum(sum_of_15))
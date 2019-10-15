""" Practice: 
girls = ["Linh", "Minh", "Long"]

fmt_str = "Hi, {}"

for girl in girls:
    print(fmt_str.format(girl))


###Naming: 

a = list('python') #avoid
print(a)


name_list = list("Nguyen Thanh Linh")
print(name_list)  




###Name binding + mutable , immutable

#Mutable: list, set, dict ,...
#imnutable : string ,int , tuple , complex,...
a = 1
b = a
a = 10
print(a, b)
print(id(a), id(b))


### Note: eveything in python is object 


###Shallow copy: copy 1 level
import copy
a = [1, 2, 3, [4, 5, 6]]
b = copy.copy(a)
a[3][2] = 1000
print(id(a), id(b))
print(a, b)

###Deep copy: copy all level
c = copy.deepcopy(a);
print(c) """

###################################################################################

"""
### keyword "in", "sorted(list)": return new list containing all items of old list 
### reserve(): 

a = [1, 2, 3, 10, 11, 8]
#b = a.sort() # --> return None
print()

print(sorted(a))
a.reverse()
print(a)



### del keyword :  Change original list
#remove(value): 
#pop(index):  --> return item(default last)
B = [2, 4, 6, 8]
temp = B.pop(0)
print(temp, B)
A = [2, 4, 6, 8]
temp2 = A.remove(4)
print(temp2, A)   """


#######################################################################################


"""Iterable: str, list , generator, .... """

# l = list(range(1,10,2))

# for item in l:
#     print(item)
# print("--------")
# for num in range(0, 10):
#     print("{0} ".format(num))

# girls = ['hoa','hue','trang']
# for girl in girls:
#     print("Hi, {}".format(girl.title()), end="-")



"""enumrate(list): return tuple ( pairs of {key: value} )"""
# girls = ["Linh", "Minh", "Long"]

# for index,girl in enumerate(girls):
#     print(index, girl)


"""If + else"""
# x = 9
# if x % 2 == 0:
#     print('true')

# else:
#     print('false')

# x = 30

# if x % 3 == 0:
#     print("buzz")
# elif x % 5 == 0:
#     print("fizz")
# elif x % 15 == 0:
#     print("FizzBuzz")

# l = [1, 2, 3]
# s = "Py"
# if l:
#     print("a")
# if s:
#     print("b")

# res = []

# for numb in range(0, 101):
#     if numb % 15 == 0:
#         res.append(numb);
# print(res)


# res = 0

# for numb in range(0, 1000):
#     if numb % 3 == 0 or numb % 5 == 0:
#         res += numb
# print(res)


# count = 0

# for a in range(1, 100):
#     for b in range(1, 100):
#         for c in range(1, 100):
#             if a + b + c == 24 and a * a + b * b == c * c:
#                 count += 1
#                 print("a = {}, b = {}, c = {}".format(a, b, c))

# print(count)


# """break ,continue"""

# for i in range(0, 21):
#     if i < 10:
#         # break
#         continue
#     print(i)


# for i in range(0, 10):
#     pass # do nothing



"""List comprehension """
# lst_comprehension = [i for i in range(20) if i % 2 == 0]
# print(lst_comprehension)
# print([i*2 for i in range(10)])


# lst = [2 for _ in range(10)]    #pythonic
# print(lst)


# print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))

# result = [[a, b, c] for a in range(1, 10) 
#                         for b in range(1, 10) 
#                             for c in range(1, 10) 
#                                 if a + b + c == 12 and a**2 + b**2 == c ** 2]
# print(result)
# print(len(result))


"""While-loop"""

# i = 0
# while i < 10:
#     i -= 2
#     print(i)

# res = i = 0
# while i < 1000:
#     if i % 3  == 0 or i % 5 == 0:
#         res += i
#     i += 1

# print(res)


"""Pythonista, more pythonic"""
# import string 

# lst  = list(string.ascii_lowercase)
# print(lst)
# res = 0

# s = "python"

# for index, char in enumerate(lst):
#     for char2 in s:
#         if char  == char2:
#             res += index + 1

# print(res)

a_ = 1
b = 2
print(a_ + b)

_sum = 1 #private
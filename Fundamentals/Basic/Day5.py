'''
- Dict, set , file I/O, Debugging
'''

# D = {}
# print(D, type(D))

# eng2sp = {}
# eng2sp['one'] = 'uno'
# eng2sp['second'] = 'dos'

# print(eng2sp)

'''Note: -The order of the pairs {key: value}
            may not be what was expected 

    -Benefit of dictionary: very fast, implemented by a technique: hashing


    -Dictionary accesses with keys , not with indices

    - Dict can't index or slice != 'string, list, tuple'

    -key of dict must be immutable ( !(list, dict , set))
    -value of dict can be everything
'''
# dict_ = {
#     1 : 'one',
#     2 : 'two',
#     3 : 'three'
# }
# print(dict_, dict_[1])
# # del dict_[1]
# dict_[1] = 'Linh'
# dict_[2] += "minh"
# print(dict_, len(dict_))


'''
*** dictionary methods: 
- keys() method: called 'view'
- values() method: 
- items() method: return tuples(key : value)
'''
dict_ = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
}

# for key in dict_.keys(): #the order of the key's is not defined
#     print('Got key ', key, ' which map to value ', dict_[key])

# for item in dict_.items():
#     print('item ', item)

# for (k, v) in dict_.items():
#     print('Key ', k, ' Value ', v)

# print(1 not in dict_)
# keys = list(dict_.keys())
# print('Keys of dict are: ', keys)
# print(dict_.pop(1))
# print(dict_)
# dict_.update({4 : 'four'})
# dict_.update({'Linh' : 'Minh'})

# print(dict_)

'''
*** Aliasing and copying ***
- dictionary is mutable
----> whenever 2 values refer to the same obj ,
changes to one affect the other

-copy() method: 
'''

# opposites = {
#     'up' : 'down',
#     'high' : 'low',
#     'true' : 'false'
# }

# alias = opposites #same memory address
# copy = opposites.copy() # shallow copy

# print(id(alias), id(opposites), id(copy))

# alias['true']  = 1
# print(opposites['true'])


'''
-Counting letters
'''

# letters_counts = {}
# for letter in "Linh":
#     letters_counts[letter] = letters_counts.get(letter, 0) + 1

# letter_items = list(letters_counts.items())
# letter_items.sort()

# print(letter_items)
# print(letters_counts)

# inp = str(input("Enter a string: ")).lower()

# letter_counts = {}

# for letter in inp:
#     if letter != ' ':
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

# # print(letter_counts)
# letter_items = list(letter_counts.items())
# letter_items.sort()

# res = dict(letter_items)
# for key, value in res.items():
#     print(key, value)

'''
-Dict comprehension
- zip() method:is to map the similar index of multiple containers
'''

# dict_ = {k : v for k, v in zip('abcde', range(5))}
# print(dict_)

# l1 = [1, 2, 3, 4]
# l2 = ['one','two','three']
# l3 = ('mot','hai','ba')

# for i in zip(l1, l2, l3):
#     print(i)



'''
*** Set ***
- is mutable, iterable
- set only contains immutable elements (!(list, dict, set))
- key of dictionary has type is set
-union() method: Return the union of sets as a new set. <=> '|' operator
'''

# s = set([1, 2, 3])
# print(type(s))
# print(s)

# for numb in s:
#     print(numb)

# lst = [1, 2, 3]
# s = set(lst)

# s1 = {2, 3 , 4}
# print(s.union(s1))
# print(s1.difference(s))

# a = 1
# b = 2

# print(a.__add__(b))
# print(s ^ s1)  # symmetric_difference
# print(s & s1)
# print(s | s1)

# L1 = [1, 2, 3, 4, 5, 6]
# L2 = [3, 4, 5, 6, 7, 8, 9, 10]

# print('Both: ', list(set(L1) & set(L2)))


# while True:
#     word = str(input("Enter a random string: ")).lower()
#     num =   dict([(i, ord(i) - 96) for i in word])
#     print(num)


# x = [2, 8, 1, 4, 6, 3, 7] 

# print('Sorted list returned: ', sorted(x))
# print('Reserve sort: ', sorted(x, reverse = True))
# print("The original list not modified: ", x)

# x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6} 
# y = ['aababa', 'acn', 'afdsv']

# print('Sort with len: ',sorted(y, key = len))

# def func(x):
#     return x % 2 
# lst = [2, 4, 5 ]
# print('Sorted with key: ', sorted(lst, key = func))

# s = 'Linh Mi'
# res = set(s)
# print(res)

# s = '1.00.2'

# a = s.split('.')
# print(int (a[1]))

# dict_ = {}
# names = ["doc", "doc", "image", "doc(1)", "doc"]
# dict_.k


# res = [[1, 2, 3], [4, 5, 6]]

word = "abacaba"
# theJanitor(word) = [7, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
tmp = word[::-1]

res = [0] * 3
print(set(word))
for i in set(word):
    res[ord(i) - 97] = len(word) -word.index(i) - tmp.index(i) 
    print(word.index(i) ,  word[::-1].index(i))
print(res)
print(word)
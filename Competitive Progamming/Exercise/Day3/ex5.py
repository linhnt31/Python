'''
T5
Luyện tập dùng list comprehension với các câu hỏi sau:
Tạo 1 list chứa N số 2
Tạo 1 list chứa các số nguyên dương dưới 100, chia hết cho 3 hoặc 5
Tạo ra 1 list có dạng như sau: ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN], với N = 20
Tạo 1 list chứa N số nguyên ngẫu nhiên, gợi ý sử dụng thư viện random: import random
'''

''' n so 2 '''

inp = int(input("Enter a value : "))

lst1 = [2 for _ in range(inp)]
print(lst1)  #n = 5 --> output: [2, 2, 2, 2, 2]


'''Tạo 1 list chứa các số nguyên dương dưới 100, chia hết cho 3 hoặc 5'''
lst2 = [i for i in range(0, 100) if i % 3 == 0 or i % 5 == 0]
print(lst2)
# # Result: [0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99]


"""Tạo ra 1 list có dạng như sau: ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN], với N = 20"""

res = []
step = 6
numb_str = ['1', '3', '5', '7', '9']
for _ in range(0, 21):
    for string in numb_str:
        res.append(string  * step)
    step += 6

print(res)   



"""Tạo 1 list chứa N số nguyên ngẫu nhiên, gợi ý sử dụng thư viện random: import random"""

import random

lst = [random.randrange(0, 100) for i in range(0, 10)] #[14, 19, 85, 82, 0, 54, 43, 32, 3, 45]
print([random.randint(0, 10) for _ in range(0, 10)])
print(lst)
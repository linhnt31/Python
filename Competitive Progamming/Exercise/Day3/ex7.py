'''
BT7
Viết chương trình tính tổng và tích tất cả các số trong 1 list: dùng vòng lặp, ko dùng hàm có sẵn (sum)
# Can use sum() function
'''
import random as rd

sum_of_list = 0
multiple_of_list = 1

#initial a random lsit
numbs = [rd.randint(1, 20) for _ in range(0, 10)]

for numb in numbs:
    sum_of_list += numb
    multiple_of_list *= numb

print("My list: {}".format(numbs))
print("Sum of list: {}".format(sum_of_list))
print("Multiple of list: {}".format(multiple_of_list))

#In a 1 case
#Output:
# My list: [7, 7, 18, 2, 15, 19, 10, 15, 20, 7]
# Sum of list: 120
# Multiple of list: 10557540000
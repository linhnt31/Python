'''
BT8
Viết chương trình tìm số lớn nhất và nhỏ nhất trong 1 list chứa cả kiểu int và float, ko dùng hàm có sẵn (max, min)
'''
import math 
#initial a random list

numbs = [1, 3.3, 5.6 , 8, 9.7, 2.5, -0.9]
max_of_list = -999999999999999999999999
min_of_list = 9999999999999999999999

for numb in numbs:
    if max_of_list < numb:
        max_of_list = numb
    if min_of_list > numb:
        min_of_list  = numb 

print('Max of list: {}'.format(max_of_list))
print('Min of list: {}'.format(min_of_list))

# Max of list: 9.7
# Min of list: -0.9
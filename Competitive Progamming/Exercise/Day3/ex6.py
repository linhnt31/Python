'''
BT6
Tính tổng tất cả các số trong kết quả của phép tính 2**10000
'''

inp = 2 ** 10000

sum_of_element = 0

while inp > 0:
    sum_of_element += inp % 10
    inp //= 10


print("Result: {}".format(sum_of_element))
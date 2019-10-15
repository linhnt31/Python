'''
BT7:
Viết code sinh các số nguyên tố dưới 10000, lưu giữ kq vào 1 list.
'''

prime_lst = []
prime_lst.append(2)

for numb in range(3, 100):
    count = 0
    for i in range(2, numb):
        if numb % i == 0:
            count += 1
    if count == 0:
        prime_lst.append(numb)

print(prime_lst) #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
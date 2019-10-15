'''
BT6:
Viết code sinh các số fibonanci dưới 1000, lưu giữ kq vào 1 list.
'''

fibonanci_range = []

numb_one = 0
numb_two = 1

fibonanci_range.append(numb_one)
fibonanci_range.append(numb_two)

while True:
    temp = numb_one + numb_two
    if temp > 1000:
        break
    numb_one = numb_two
    numb_two = temp
    fibonanci_range.append(temp)

print(fibonanci_range) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
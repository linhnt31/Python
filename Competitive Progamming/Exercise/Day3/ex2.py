'''
BT2:
Sử dụng vòng lặp in ra các số từ 1 đến 100, 
-nếu số đó chia hết cho 3 thì thay bằng Buzz, 
-chia hết cho 5 thì thay bằng Fizz,
-nếu chia hết cho cả 3 và 5 thì thay bằng FizzBuzz.
 -Đồng thời, lưu giữ kết quả đạt được vào 1 list
'''

res = []

for numb in range(1,101):
    if numb % 15 == 0:
        res.append("FizzBuzz")
    elif numb % 5 == 0:
        res.append("Fizz")
    elif numb % 3 == 0:
        res.append("Buzz")
    else:
        res.append(numb)

print(res)
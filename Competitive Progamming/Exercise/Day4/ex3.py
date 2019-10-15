'''
BT3:
Nhập 1 số nguyên trong đoạn từ 1 đến 12, thực hiện trả về tuple bao gồm số ngày và tên tiếng anh tương ứng
input: 1
output: (31, "January")
nếu nhập ngoài khoảng đó thì thông báo nhập lại, đến khi nào đúng thì thôi.
'''

numb = int(input("Enter a number: "))

while True:
    if numb < 1 or numb > 12:
        print("Wrong input !!! Please check it again")
        numb = int(input("Enter a number: "))
    else:
        break

day_and_month = ((31, 'January'), (28, 'February'), (31, 'March'), (30, 'April'),\
                (31, 'May'), (30, 'June'), (31, 'July'), (31, 'August'), (30, 'September'),\
                (31, 'October'), (30, 'November'), (31, 'December'))

for index, month in enumerate(day_and_month):
    if index + 1 == numb:
        print(day_and_month[index])


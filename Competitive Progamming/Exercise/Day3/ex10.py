'''
BT10
Nếu lần lượt cho các giá trị trong bảng chữ cái tiếng Anh như sau: 
a = 1, b = 2, c = 3, .... thì tổng giá trị của các từ khi quy đổi ra số là như sau:
abc = 1 + 2 + 3 = 6
defgh = 4 + 5 + 6 + 7 + 8 = 30 
....
Hỏi các từ sau có giá trị là bao nhiêu: python, patience, documents, students, homework,
 practice, success, english, university, congratulation
'''
import string 

lst  = list(string.ascii_lowercase)
inp_string = str(input("Enter a string: "))

res = 0

for index, char in enumerate(lst):
    for char2 in inp_string:
        if char  == char2:
            res += index + 1

print("Sum of values: {}".format(res))
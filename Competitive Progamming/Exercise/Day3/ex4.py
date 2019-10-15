'''
BT4
Có bao nhiêu bộ ba A, B, C thỏa mãn điều kiện sau:

A, B, C đều là số nguyên dương
A + B / C = 10 ---> AC + B = 10C
Lưu các giá trị tìm đc vào 1 list lớn chứa các list con: vd: [[9, 1, 1], ....]

'''

res = []
count = 0
for a in range(0, 11):
    for b in range(0, 11):
        for c in range(0, 11):
            if a*c + b == 10*c:
                res.append([a, b, c])
                count += 1

print("Result: {}".format(res))
print("number of pairs: {}".format(count)) #48
                    


#2019 : Ki Hoi --> Nhap 1 nam bat ki --> can chi ?

# Canh - 0; Tân - 1, Nhâm - 2, Quý - 3, Giáp - 4, Ất - 5, Bính - 6, Đinh - 7, Mậu - 8; Kỷ - 9.
# Tí – 0; Sửu – 1, Dần – 2; Mão – 3, Thìn – 4, Tỵ - 5, Ngọ - 6, Mùi – 7, Thân – 8, Dậu – 9, Tuất - 10, Hợi – 11.


year  = int(input("Enter a year: "))

can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu","Kỉ"]

table1_chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ ", "Mùi"]
table2_chi = ["Tí", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi","Thân", "Dậu", "Tuất", "Hợi"]
table3_chi = ["Thìn", "Tỵ", "Ngọ", "Mùi","Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mão"]


res = ""

if(year < 10):
    if year % 3 == 0:
        res += can[year] + " " + table1_chi[year % 12]
    elif year % 3 == 1:
        res += can[year] + " " + table2_chi[year % 12]
    else:
        res += can[year] + " " + table3_chi[year % 12]
else:
    tail_numbers = year % 100
    head_numbers = year // 100

    if (head_numbers) % 3 == 0:
        res += can[year % 10] + " " + table1_chi[tail_numbers % 12]
    elif (head_numbers) % 3 == 1:
        res += can[year % 10] + " " + table2_chi[tail_numbers % 12]
    else :
        res += can[year % 10] + " " + table3_chi[tail_numbers % 12]

print(res)
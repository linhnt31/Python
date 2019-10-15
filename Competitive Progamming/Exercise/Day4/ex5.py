'''
BT5:
Trả về 1 list n tuple được định nghĩa như sau:
years = [(1900, "Canh Tí"), ... (2019, "Kỷ Hợi")]
với năm chạy từ 1900 đến 2019, output yêu cầu trả về đúng như format bên trên, bao gồm năm và can chi tương ứng
Chú ý viết hoa các chữ cái đầu.
'''

def check_canchi(year):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu","Kỉ"]

    table1_chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ ", "Mùi"]
    table2_chi = ["Tí", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi","Thân", "Dậu", "Tuất", "Hợi"]
    table3_chi = ["Thìn", "Tỵ", "Ngọ", "Mùi","Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mão"]

    can_chi = []

    if(year < 10):
        if year % 3 == 0:
            can_chi.append(can[year] + " " + table1_chi[year % 12])
        elif year % 3 == 1:
            can_chi.append(can[year] + " " + table2_chi[year % 12])
        else:
            can_chi.append(can[year] + " " + table3_chi[year % 12])
    else:
        tail_numbers = year % 100
        head_numbers = year // 100

        if (head_numbers) % 3 == 0:
            can_chi.append(can[year % 10] + " " + table1_chi[tail_numbers % 12])
        elif (head_numbers) % 3 == 1:
            can_chi.append(can[year % 10] + " " + table2_chi[tail_numbers % 12])
        else :
            can_chi.append(can[year % 10] + " " + table3_chi[tail_numbers % 12])

    return "".join(can_chi)

years = []
for year in range(1990, 2020):
    years.append((year, check_canchi(year)))

print(years)


"""
BT1: cho 1 biến data kiểu string như bên dưới
data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''
# https://www.poetrysoup.com/poem/cross_my_heart_609765
Yêu cầu: giải mã mật thư, lấy tất cả các chữ cái đầu của từng dòng rồi ghép lại để được 1 câu """


data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''

res = '' #not encourage

for string in data:
    if string.isupper():
        res += string

print("Result: "+ res)

# Result: CROSSMYHEART
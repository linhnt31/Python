'''
*BT4:
Cho đoạn bài hát sau
Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 

-làm rõ lời bài hát bằng cách loại bỏ toàn bộ các số và kí tự puntuation :)
-puntuation là gì?
'''
    
import string

lyrics = '''
Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 
'''

lines = lyrics.split('\n')
# print(lines)

new_lines = []
for line in lines:
    for char in line:
        if char not in string.punctuation \
            and not char.isdigit():
            new_lines.append(char)
    new_lines.append('\n')
        
new_lyrics = "".join(new_lines)
print(new_lyrics.strip())
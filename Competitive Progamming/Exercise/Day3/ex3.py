'''
BT3
Viết chương trình loại bỏ phần mở rộng của 1 tên file bất kì 
VD: newfile.txt -> newfile, photoshop.psd -> photoshop, word.docx -> word, ....
'''

inp_string = str(input("Enter a random string: "))
len_of_str = len(inp_string)
res = ''

for index in range(len_of_str - 1, -1, -1):
    if inp_string[index] == '.':
        res += inp_string[index-1::-1]
        break

print("Result: "+ res[::-1])


#fix exercises


'''BT1:
 Viết code kiểm tra 1 string có phải là palindrome hay ko?
 (string đối xứng, viết xuôi hay viết ngược đều như nhau, ko kể viết hoa hay viết thường)
 '''

inp_str = str(input("Enter a random string: "))

reverse_str = inp_str[::-1]
check = True

if inp_str == reverse_str:
    print('{} is palindrome'.format(inp_str))
else:
    print('String is not palindrome'.format(inp_str))
# string1 = "PythonJava123"
# print(string1)
# print(string1*3)

# a = 'python' 'pk'              
# b = 'T3H'
# print(a+b)
# # print(a)

# print("I'm a student")
# print('I"m a student')


""" escape chars: '\' (backslash)"""

# s = "I'm a student and I\"am learning python \" Linh"
# s1 = """Linh""" 
# s1 = s+s1
# # print(s)
# print(s1)

"""String method"""

"""
#capitalize()
s = "python go java"
print(s.capitalize())

#title(): in hoa ki tu sau space
print(s.title())

#startWith + endWith
print(s.startswith("pyt"))
print(s.endswith("Hello"))

#find(): return index else cant find --> return -1
print(s.find('java'))

#upper + lower
print(s.upper())


'''whitespace : \t, \n, space'''
print("{} PTIT".format("I love"))
print("{0} Cong Nghe Buu Chinh {1}".format("Hoc vien","Vien Thong"))  """




"""Slicing of string"""
#Palindrome
s = 'aba'
print(s == s[::-1])
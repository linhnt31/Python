'''
- Solution: use queue , create only list has 10 elements
'''

f = open('ex1.txt') #reading

content = f.read()
content = content.strip().split()
f.close()
print(content[-1 : -11 : -1])
# print(content)

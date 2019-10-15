# my_file = open('test.txt','w')
# my_file.write('My first file written from Python\n')
# my_file.write('Hello File I/O')

# mynewhandle  = open('test.txt', 'r')
# while True: # keep reading forever
#     the_line = mynewhandle.readline() #Try to read next line
#     if len(the_line) == 0: 
#         break
#     print(the_line, end='')
# my_file.close()

'''
Turning a file into a list of lines
'''

# my_file = open('test.txt', 'r')
# lst = my_file.readlines()
# my_file.close()

# print(lst)

'''
Reading the whole file at once
'''

 
demo = open('somefile.txt', 'w')
demo.write('Im learning python')

# demo = open('somefile.txt')
# content = demo.read()
# demo.close()

with open('somefile.txt', 'r') as f:
    content = f.read()
    
words = content.split()
print('There are {} words in the file'.format(len(words)))
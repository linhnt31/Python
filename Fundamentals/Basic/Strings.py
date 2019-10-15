"""
string = 'doesn\'t'
print(string)
"""

#String literals can spread multiple lines
#If we dont have "\" --> the result will stand a new line
print("""\
    Usage: thingboards [Option]
    hello
    python3
""")

string1 = "Py"
string2 = "thon"

#auomatically concatenate
string3 = "Li" "nh"
print(string1 +  string2)
print(string3)

#length of strings
leng_of_string = "Linh Nguyen Thanh"
print("length of string %s is %d" % (leng_of_string,len(leng_of_string)))

""" String formating using %  and .format """ 
#New version: {}      #old version: %s %d 
print("String formating: {1} {0}".format('test',1999))


""" padding and aligning strings """
#Align right
print("New style: {:>10}".format('test'))
print('Old style: %10s' % ('test'))

#Align left + center
print("New style: {:_^10}".format('test'))
print('Old style: %-10s' % ('test'))

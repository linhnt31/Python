"""
#Referrence:
http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html
"""

def toStr(n, base):
    convertString = "0123456789ABCDEF"

    if n < base:
        return convertString[n]
    return toStr(n // base, base) + convertString[n % base]

if __name__ == "__main__":
    print("{} converted to {}".format(8, toStr(8, 2)))
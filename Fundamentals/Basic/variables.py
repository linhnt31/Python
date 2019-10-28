""" Reference: https://www.geeksforgeeks.org/global-local-variables-python/#targetText=Global%20and%20Local%20Variables%20in%20Python,use%20them%20inside%20a%20function.&targetText=If%20a%20variable%20with%20same,and%20not%20the%20global%20value. """

#A value can't be both local and global inside  of a function.

"""   
def f():
    global s
    print(s)
    s = "Hunter city"
    print(s)

s = "I love Vietnam"
f()

"""


"""Link: https://app.codesignal.com/challenge/E6XCNZEDWrNCboYAs  """
res = 0
tmp = 0

def piecesOfDistinctLengths(strawLength):
    global res
    global tmp
    if strawLength == 0:
        return res
    else:
        if strawLength > 0:
            res += 1
            tmp += 1
            return piecesOfDistinctLengths(strawLength - tmp)
        res -= 1
        tmp -= 1
        return piecesOfDistinctLengths(strawLength + tmp)
    return res

if __name__ == "__main__":
    print(piecesOfDistinctLengths(20))
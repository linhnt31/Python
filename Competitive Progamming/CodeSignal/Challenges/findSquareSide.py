""" Link: https://app.codesignal.com/challenge/mCGWhBSaQ2nY2ZoiC """

def findSquareSide(x, y):
    res = 99999
    for i in range(len(x) - 1):
        tmpX = x[i] - x[i+1]
        tmpY = y[i] - y[i+1]
        res = min(res, tmpX*tmpX + tmpY*tmpY)
    return res


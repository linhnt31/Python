"""
#Referrences: 
http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html

"""

def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    return numList[0] + listSum(numList[1:])

if __name__ == "__main__":
    numList = [1, 2 , 3, 4, 5]
    print('Sum of list is {}'.format(listSum(numList)))
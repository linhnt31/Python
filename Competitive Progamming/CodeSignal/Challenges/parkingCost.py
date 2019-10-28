""" Link: https://app.codesignal.com/challenge/vjsPvZ3hv5ZdxxYzC?solutionId=ZefKrB3tSeLcteyb7 """


def parkingCost(timeIn, timeOut):
    h = int(timeOut[:2]) - int(timeIn[:2])
    m = int(timeOut[3:]) - int(timeIn[3:])
    
    res = h * 60 + m 
    if res % 10 != 0:
        res += (10 - res % 10)
    if res <= 30:
        return 0
    elif 30 < res <= 120:
        return (res - 30) // 10
    return 9 + ((res - 120)//10) * 2

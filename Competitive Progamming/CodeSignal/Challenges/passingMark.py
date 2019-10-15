''' 
- Link: https://app.codesignal.com/challenge/ot8fqNgrJmjQrGwpk
'''

def passingMark(passMark, grades):
    grading_scale = {
        'A' : 5,
        'B' : 4,
        'C' : 3,
        'D' : 2, 
        'E' : 1
    }
    sum = 0
    for grade in grades:
        sum += grading_scale[grade]
    return (sum / len(grades)) >= passMark

"""
- Link: https://app.codesignal.com/tournaments/Zz5XycZeuGBmYtS76/C
"""

def crossingSum(matrix, a, b):
    sum_ = 0
    
    for i in range(0, len(matrix[0])):
        sum_ += matrix[a][i]
        
    for i in range(0, len(matrix)):
        sum_ += matrix[i][b]
        
    sum_ -= matrix[a][b]
    
    return sum_
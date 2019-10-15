'''
- Link: https://app.codesignal.com/challenge/9kfQBhmWkTrC9aJte
'''

#Solution: 
def chessBoardCellColor(cell1, cell2):
    x = ord(cell1[0]) - ord('A') + ord(cell1[1]) - 48
    y = ord(cell2[0]) - ord('A') + ord(cell2[1]) - 48
    
    return (abs(x - y)) % 2 == 0
"""
-Link: https://app.codesignal.com/challenge/b4eAriXPbJypzfeXL
"""

def onboard(a,n):
    if ord("a")<=a<=ord("h") and 1<=n<=8:
        return True
    return False
    
def chessKnightMoves(cell):
    move = 0
    cell = [ord(cell[0]),int(cell[1])]
    moves = [[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[-2,1],[1,-2],[2,-1]]
    for m in moves:
        if onboard(cell[0]+m[0],cell[1]+m[1]):
            move+=1
    return move
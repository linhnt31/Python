"""
-Link: https://app.codesignal.com/challenge/yevt2AXgvguitTzzu
"""

def replaceMiddle(arr):
    size = len(arr)
    if size % 2 != 0:
        return arr
    else:
        middle = arr[size // 2]+arr[size // 2-1]
        return arr[0:size // 2 - 1]+[middle]+arr[size // 2 + 1:]
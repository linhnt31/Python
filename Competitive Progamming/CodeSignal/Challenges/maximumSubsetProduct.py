"""
-Link: https://app.codesignal.com/challenge/gnc8fMQSsxshLj9BY
"""

def maximumSubsetProduct(a):
    ans = -float('inf')
    count = 0
    for val in a:
        if val > 0:
            continue
        ans = max(ans, val)
        count += 1
    if count % 2 == 0 or len(a) == 1:
        return 1
    return ans


if __name__ == "__main__":
    a = [-4, -2, 10, 20, -3]
    print('Result: ',maximumSubsetProduct(a))
    
        
"""
- Find Sets Of Numbers That Add Up To total

"""

def dp(arr, total, i, memo):
    key = str(total)+":"+str(i)

    if key in memo:
        return memo[key]
    
    if total == 0:
        return 1 
    elif total < 0:
        return 0
    elif i < 0 or i > len(arr):
        return 0
    elif arr[i] > total:
        to_return =  dp(arr, total, i - 1, memo)
    else:
        to_return =  dp(arr, total - arr[i],i - 1, memo) + dp(arr, total,i - 1, memo)
    
    memo[key] = to_return
    return to_return 

if __name__ == "__main__":
    print(dp([2,4,6,10], 6, 3, {}))
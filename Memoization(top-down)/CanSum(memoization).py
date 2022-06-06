#  Optimized Solution

def canSum(target,arr,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for i in arr:
        rem = int(target) - int(i)
        if canSum(rem,arr,memo) == True:
            memo[target] = True
            return True
    memo[target] =  False
    return False
        


print(canSum(7,[5,3,4,7]))
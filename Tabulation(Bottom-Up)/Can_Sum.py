#o(mn) Time complexity

def func(target,arr):
    dp = [False for i in range(target+1)]
    dp[0] = True
    for i in range(len(dp)):
        if dp[i] == True:
            for j in arr:
                if i+j < len(dp):
                    dp[i+j] = True
    return dp[target]


print(func(7,[5,3]))
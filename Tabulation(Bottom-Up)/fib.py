# o(n) complexity

def fib(x):
    dp = [0] * int(x+1)
    dp[1] = 1
    for i in range(2,x+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[x])

fib(200)

# def func(x):
#     if x == 0:
#         return 0
#     if x == 1 or x==2:
#         return 1
#     else:
#         return func(x-1) + func(x-2)
# print(func(7))
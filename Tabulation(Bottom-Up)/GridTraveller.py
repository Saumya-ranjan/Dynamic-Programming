# Basic By Memoization

# def GridTraveller(r,c):
#     if r==0 or c == 0:
#         return 0
#     if r == 1 and c==1:
#         return 1
#     else:
#         return GridTraveller(r-1,c) + GridTraveller(r,c-1)
# print(GridTraveller(3,3))


# By Tabulation:

def GridTraveller(r,c):
    dp = [[0 for i in range(c+1)] for i in range(r+1)]
    dp[1][1] = 1
    for i in range(r+1):
        for j in range(c+1):
            curr = dp[i][j]
            if i+1 <= r:
                dp[i+1][j] += curr
            if j+1 <= c:
                dp[i][j+1] += curr
    return dp[r][c]


print(GridTraveller(3,3))
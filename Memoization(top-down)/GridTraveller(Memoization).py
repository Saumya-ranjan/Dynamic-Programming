# Classic Way to solve Grid Traveler Problem:
# Time Complexity = o(2^m+n)
# Space Complexity = o(m+n)

# def GridTraveler(m,n):
#     if m==1 and n==1:
#         return 1
#     if m==0 or n==0:
#         return 0
#     else:
#         return GridTraveler(m-1,n) + GridTraveler(m,n-1)
# print(GridTraveler(3,8))



# By Memoization Efficient formula:

def GridTraveler(m,n,memo={}):
    keys = str(m) + ',' +str(n)
    if keys in memo:
        return memo[keys]
    if m == 1 and n ==1:
        return 1
    if m==0 or n==0:
        return 0
    else:
        memo[keys] = GridTraveler(m-1,n,memo) + GridTraveler(m,n-1,memo)
    return memo[keys]
     

print(GridTraveler(3,3))
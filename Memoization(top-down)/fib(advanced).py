#Classic Implemenation of fibonnaci series

# def func(n):
#     if n <= 2:
#         return 1
#     else:
#         return func(n-2) + func(n-1)


# print(func(int(input("Input the number: "))))


# It have o(2^n) time complexity
# That really means that if we take fib(50) it goes like: 2^50
#That is roughly 1125899906842624 steps for the computer
# so this classic implementation only works for small NUmbers.



# This is the efficient code for fibbonacci series :
# saving the precalculated roots in memo and using it.

def func(n,memo = {}):   #Time complexity: o(n)
    if n in memo:
        return memo[n] 
    if n <= 2:
        return 1
    else:
        memo[n] =  func(n-2,memo) + func(n-1,memo)
    return memo[n]


print(func(int(input("Input the number: "))))
 
 # we bring it down from exponential time complexity to linear 
 # time complexity o(n) 
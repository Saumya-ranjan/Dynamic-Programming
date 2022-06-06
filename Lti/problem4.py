# max no. of pearls - input 1 
# starting magnificient coeff of pearl - input 2
# ending magnificient coeff of pearl - input 3

# 3   7    9    ---> 5        7  8  9  78  79 789 89  


# Explanation:
# Input: n = 3, start = 6,end = 9
# The necklace can be formed in the following ways:
# Output: 34
# The necklaces of length one that can be formed are { “6”, “7”, “8”, “9” }.
# The necklaces of length two, that can be formed are { “66”, “67”, “68”, “69”, “77”, “78”, “79”, “88”, “89”, “99” }.
# The necklaces of length three, that can be formed are { “666”, “667”, “668”, “669”, “677”, “678”, “679”, “688”, “689”, “699”, “777”, “778”, “779”, “788”, “789”, “799”, “888”, “889”, “899”, “999” }.
# Thus, in total, the necklace can be formed in (4+10+20 = 34 ) ways.

# Input: N = 1, L = 8, R = 9
# Output: 2
# Explanation:
# The necklace can be formed in the following ways: {“8”, “9”}. 


def func(n,start,end):
    arr = ""
    arr1 = []
    for i in range(start,end+1):
        arr+=str(i)
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    print(arr1)




func(3,6,9)

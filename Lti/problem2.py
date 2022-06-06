def func(arr):
    temp = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j] and abs(arr[i] - arr[j]) > temp:
                temp  = abs(arr[i] - arr[j])
    print(temp)

            


func( [2, 3, 10, 6, 4, 8, 1])
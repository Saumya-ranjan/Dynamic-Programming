def func(arr):
    arr1= []
    odd = []
    even = []
    arr.sort()
    for i in arr:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
    if len(even) != len(odd):
        print("Wrong Input")
        return False
    if arr[0]%2 == 0:
        for i in range(len(odd)):
            arr1.append(even[i])
            arr1.append(odd[i])
    else:
        for i in range(len(odd)):
            arr1.append(odd[i])
            arr1.append(even[i])
    print(arr1)
     

func([9, 8, 13, 2, 19, 14])
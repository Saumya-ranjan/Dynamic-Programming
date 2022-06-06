def func(x):
    arr = []
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            arr.append(x[i:j])
    print(arr)



func('abcdefg')
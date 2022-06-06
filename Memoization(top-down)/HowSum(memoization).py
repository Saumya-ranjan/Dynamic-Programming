def func(target,arr):
    if target == 0 :
        return []
    if target < 0:
        return None
    for i in arr:
        temp = target - i
        result =  func(temp,arr)
        if result != None:
            return [result,i]
    return None


print(func(7,[2,3]))
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min_num = max_num = L[0]
    for it in L:
        if min_num > it:
            min_num = it
    for it in L:
        if max_num < it:
            max_num = it
    return (min_num, max_num)
        


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

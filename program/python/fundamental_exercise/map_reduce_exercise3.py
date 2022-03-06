from functools import reduce

def modi(tmp):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    return DIGITS[tmp]

def multi10(x, y):
    return x*10+y

def multiex(x, y):
    return x*0.1+y

def str2float(s):
    list_s = s.partition('.')
    a = str(list_s[0])
    b = str(list_s[2])
    b = b[::-1]
    #print(reduce(multiex,map(modi,list_s[2])))
    return reduce(multi10,map(modi,a))+0.1*reduce(multiex,map(modi,b))

# test
print('str2float(\'123.456\') = ', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")

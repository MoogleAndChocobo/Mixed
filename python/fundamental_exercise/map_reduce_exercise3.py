from functools import reduce

def str2float(s):
    list_s = s.partition('.')
    def modi(tmp):
	data = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
	return data[tmp]

    def multi10(x, y):
	return x*10+y
	
    def multiex(x, y):
	return x*0.1+y
    return reduce(multi10, map(modi, list_s[0]))+'.'+reduce(multiex,map(modi,list_s[2]))

# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

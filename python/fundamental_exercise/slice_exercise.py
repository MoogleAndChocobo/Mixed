def trim(s):
    st = 0
    en = len(s)
    while s[st:st+1] == ' ':
        st += 1
    while s[en-1:en] == ' ':
        en -= 1
    return s[st:en]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

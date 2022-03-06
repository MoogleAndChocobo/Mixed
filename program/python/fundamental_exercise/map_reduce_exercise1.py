def normalize(name):
    name = name.lower()
    tmp = name[1:len(name)]
    name = name[0:1]
    return name.upper()+tmp
  
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

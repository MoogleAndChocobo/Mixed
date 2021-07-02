'''
f = open("tmp/demo.txt", "r")
#print(f.read())
print(f.read(20))
print(f.read(8))
print(f.readline())
f.close()
'''


'''
f = open("tmp/demo.txt", "a")
f.write("\nNow the file has more contents!")
f.close()
f = open("tmp/demo.txt", "r")
print(f.read())

#'w' 写入
#'x' 创建，文件已存在返回错误
#'a' 追加
'''


import os 

'''
f = open("tmp/del.txt", "w")
f.write("xxx")
f.close()
f = open("tmp/del.txt", "r")
print(f.read())
f.close()
'''
if os.path.exists("tmp/del.txt"):
    os.remove("tmp/del.txt")


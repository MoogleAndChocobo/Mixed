def fib(maxnum):
    n, a, b = 0, 0, 1
    while n < maxnum:
        yield b
        a, b = b, a + b
        n += 1
    return "done"

for i in fib(10):
    print(i)

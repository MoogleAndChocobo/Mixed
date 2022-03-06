# 闭包(closure)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
    
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

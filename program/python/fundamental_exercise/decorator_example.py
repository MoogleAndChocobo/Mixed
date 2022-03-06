import functools

'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2021.07.05')

now()
'''

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2021.07.05')

now()

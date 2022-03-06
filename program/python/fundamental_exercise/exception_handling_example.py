#!usr/bin/python3
# -*- coding:utf-8 -*-

'exception_handling_example.py'

__author__ = 'MoogleAndChocobo'

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

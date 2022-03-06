#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'module example'

__author__ = 'MoogleAndChocobo'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello')
    elif len(args)==2:
        print('hello, %s' % args)
    else:
        print('Too many arguments!')
        
if __name__ == '__main__':
    test()



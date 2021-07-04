#!usr/bin/python3
# -*- coding: utf-8 -*-

'metaclass_example.py'

__author__ = 'MoogleAndChocobo'

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
        
class Mylist(list, metaclass=ListMetaclass)
    pass


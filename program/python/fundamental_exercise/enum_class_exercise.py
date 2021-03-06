#!usr/bin/python3
# -*- coding: utf-8 -*-

'enum_class_exercise.py'

__author__ = 'MoogleAndChocobo'

from enum import Enum, unique

#@unique
Gender = Enum('Gender', ('Male', 'Female'))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

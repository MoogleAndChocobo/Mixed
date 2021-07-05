#!/usr/bin/dev python3
# -*- coding: utf-8 -*-

__author__ = 'MoogleAndChocobo'

import os

filespath = []
for x in os.listdir('.'):
    abspath = os.path.abspath('.')
    filespath.append(os.path.join(abspath, x))
print(filespath)

filesinfo = []
for x in filespath:
    filesinfo.append(os.stat(x))

print("totol " + len(filesinfo))

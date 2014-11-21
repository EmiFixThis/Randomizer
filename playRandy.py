#! /usr/bin/env python

import random 
from math import floor, ceil, sqrt
import os
import binascii
import csv


BYTES = 2**18
itr = 0
maxItr = 255 

randData = os.urandom(BYTES)

while (itr < maxItr):
    itr = 0
    maxItr = 255

    byteDistro = {}
    byteVal = {}


    for i in randData:
        x = ord(i)

        with open('byteVal.csv', 'w') as b:
            for i in randData:
                print '{0}: {1}'.format(x, ord(i))
            f.write('str({0}' + ',' + 'str({1})' + '\n')

    
       # if x not in byteDistro:
        #    byteDistro[x] = 0
       # byteDistro[x] += 1

        #with open('fName.csv', 'w') as f:
         #   for key in byteDistro:
          #      print '{0}: {1}'.format(key, x[key])
           # f.write('str({0})' + ',' + 'str({1})' + '\n')
            itr += 1


        







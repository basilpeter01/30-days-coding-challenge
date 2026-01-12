'''
Day 8
EASY
Accepted 
10/10 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def utopianTree(n):
    h=1
    for i in range(n+1):
        if i == 0:
            h=1
        elif i%2 != 0:
            h=(2*h)
        else:
            h+=1
    return h        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

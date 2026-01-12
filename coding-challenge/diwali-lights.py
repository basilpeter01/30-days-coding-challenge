'''
day5
MEDIUM
completed 
11/11 test cases passed
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def lights(n):
    return ((2**n)-1) % (10**5)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()

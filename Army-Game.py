'''
Day-10
EASY
Not accepted
3/23 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def gameWithCells(n, m):
    if n % 2 == 0:
        rows = (n//2)
    else:
        rows = n//(2+1)

    if m % 2 == 0:
        cols = m//2
    else:
        cols = m//(2+1)

    return rows * cols

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

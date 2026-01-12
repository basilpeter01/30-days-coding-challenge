'''
Day-15
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

def strangeGrid(r, c):
    if r%2 != 0:
        return ((r-1)*5)+((2*c)-2)
    else:
        return((r-2)*5)+((2*c)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()

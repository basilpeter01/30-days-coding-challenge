'''
Day-21
EASY
Accepted
12/12 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def strangeCounter(t):
    time = 3
    while t > time:
        t -= time
        time *= 2
    return time - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

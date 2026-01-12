'''
Day-20
EASY
Not Accepted
4/28 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def getMax(operations):
    stack=[]
    lst=[]
    for i in operations:
        parts=i.split()
        if parts[0] == '1':
            stack.append((parts[1]))
        elif parts[0] == '2':
            if stack:
                stack.pop()
        else:
            if stack:
                lst.append(max(stack))
    return (lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

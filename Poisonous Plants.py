'''
Day-26
HARD
Not Accepted
28/31 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def poisonousPlants(p):
    lst=[]
    l=n
    count=0
    while True:
        for i in range(l):
            if i == 0:
                continue
            else:
                if p[i] > p[i-1]:
                    lst.append(i)
        if not lst:
            break
        for j in reversed(lst):
            p.pop(j)
        lst=[]
        count+=1
        l=len(p)
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

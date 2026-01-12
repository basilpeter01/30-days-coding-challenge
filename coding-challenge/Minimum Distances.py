'''
Day-22
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

def minimumDistances(a):
    d={}
    for i in a:
        c=a.count(i)
        if c > 1:
            d[i]=c
    if not d:
        return -1
    else:
        l=[]
        for i in d:
            a1=a.index(i)
            for j in range(a1+1,len(a)):
                if i == a[j]:
                    a2 = j
                    l.append(abs(a1-a2))
                    break
    return min(l)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

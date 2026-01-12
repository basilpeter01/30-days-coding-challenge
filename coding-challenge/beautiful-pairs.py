'''
day6
EASY
Not Accepted 
7/8 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulPairs(A, B):
    d1={}
    d2={}
    count=0
    if A == B:
        return len(B)-1
    else:
        for i in A:
            d1[i]=0
        for i in A:
            c=A.count(i)
            d1[i]=c
        for i in B:
            c=B.count(i)
            d2[i]=c
        for i in (set(A) & set(B)):
            count+=min(d1[i],d2[i])
    return count+1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

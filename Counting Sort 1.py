'''
Day-19
EASY
Accepted
6/6 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    l=[0]*100    
    for i in range (len(arr)):
        x=arr[i]
        l[x]+=1
    return l    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

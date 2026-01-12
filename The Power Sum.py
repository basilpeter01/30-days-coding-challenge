'''
Day-25
MEDIUM
Not Accepted
1/6 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def powerSum(X, N):
    sum=0
    count=0
    for i in range (X):
        for j in range(i,X+1):
            sum+=j**N
            if sum == X:
                print (sum)
                count+=1
                break
            if sum > X:
                break
        sum = 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()

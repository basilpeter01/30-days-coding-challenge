'''
Day-24
MEDIUM
Not Accepted
2/31 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def gridlandMetro(n, m, k, track):
    sum=(n-k)*m
    for i in range(k):
        r=track[i][0]
        c1=track[i][1]
        c2=track[i][2]
        k=0
        c1=m-(c1-1)
        k=m-((m-c1)+(m-c2))
        
        per_r=m-k
        sum+=per_r
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()

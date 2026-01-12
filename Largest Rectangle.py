'''
Day-16
MEDIUM 
Accepted
16/16 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def largestRectangle(h):
    stack = []
    max_area = 0
    h.append(0)
    
    
    for i in range(len(h)):
        while stack and h[i] < h[stack[-1]]:
            height = h[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

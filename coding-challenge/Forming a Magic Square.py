'''
Day-14
Medium
Accepted
23/23 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    m1=[[8,3,4],[1,5,9],[6,7,2]]
    m2=[[6,7,2],[1,5,9],[8,3,4]]
    m3=[[4,3,8],[9,5,1],[2,7,6]]
    m4=[[2,7,6],[9,5,1],[4,3,8]]
    m5=[[8,1,6],[3,5,7],[4,9,2]]
    m6=[[6,1,8],[7,5,3],[2,9,4]]
    m7=[[4,9,2],[3,5,7],[8,1,6]]
    m8=[[2,9,4],[7,5,3],[6,1,8]]
    l=[m1,m2,m3,m4,m5,m6,m7,m8]
    lst=[]
    for m in l:
        cost=0
        for i in range(3):
            for j in range(3):
                if m[i][j] == s[i][j]:
                    continue
                else:
                    cost+=abs(m[i][j] - s[i][j])
        lst.append(cost)
    return(min(lst))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
Day-23
MEDIUM
Accepted
21/21 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    l=len(s)
    stack=[]
    flag=False
    if l % 2 != 0:
        return "NO"
    else:
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack:
                    return "NO"
                p=stack.pop()
                if (i == '}' and p != '{' ) or (i == ')' and p != '(' ) or (i == ']' and p != '[' ):
                    return "NO"
    return "YES" if not stack else "NO"
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

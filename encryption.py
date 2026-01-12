'''
Day-12
MEDIUM
Not accepted 
10/13 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def encryption(s):
    
    count=0
    arr=[]
    for i in s:
        if i == " ":
            continue
        else:
            count+=1
    n=int(math.sqrt(count))
    m=n+1
    words = s.split()
    words=''.join(words)
    a=0
    b=m
    for i in range(m):
        word=words[a:b]
        arr.append(word)
        a=b
        b=b+m 
    msg=""
    for j in range(m):
        for i in arr:
            if j<len(i):
                msg+=i[j]
            else:
                continue
        msg+=" "
    return msg    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

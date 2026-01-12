'''
Day-28
EASY
Accepted
19/19 test cases passed
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    
def primeCount(n):
    p=1
    count=0
    i=2
    if n == 0 or n == 1:
        return 0
    while p<=n:
        if is_prime(i):
            p=p*i
            count+=1
        i+=1
    return count-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

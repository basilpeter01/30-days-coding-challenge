'''
Day-27
MEDIUM
Not Accepted
2/13 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def waiter(number, q):
    primes=[]
    a1=[]
    b1=[]
    ans=[]
    for n in range(2,1201):
        if len(primes) >= q:
            break
        if is_prime(n):
            primes.append(n)
        else:
            continue
    for i in primes:
        a1=[]
        b1=[]
        for j in reversed(number):
            if j % i == 0:
                b1.append(j)
            else:
                a1.append(j)            
            number.remove(j)
        if b1:
            for k in reversed(b1):
                ans.append(k)
        number=[]
        if a1:
            for k in (a1):
                number.append(k)
    if a1:
        for i in reversed(a1):
            ans.append(i)     
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

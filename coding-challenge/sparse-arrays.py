"""
day3
MEDIUM
COMPLETED 
13/13 test cases passed
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def matchingStrings(stringList, queries):
    d={}
    for i in queries:
        d[i]=0
    set_queries = set(queries)
    for i in set_queries:
        for j in stringList:
            if i == j:
                d[i]+=1
    r=[]
    for i in queries:
        r.append(d[i])
    return r                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

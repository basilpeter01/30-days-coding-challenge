'''
Day 9
MEDIUM
Accepted
7/7 test cases passed
'''
# #!/bin/python3

import math
import os
import random
import re
import sys
def organizingContainers(container):
    n = len(container)
    container_sums = []
    for i in range(n):
        total = 0
        for j in range(n):
            total += container[i][j]
        container_sums.append(total)

    type_sums = []
    for j in range(n):
        total = 0
        for i in range(n):
            total += container[i][j]
        type_sums.append(total)

    used = [False] * n
    possible = True

    for i in range(n):
        matched = False
        for j in range(n):
            if not used[j] and container_sums[i] == type_sums[j]:
                used[j] = True
                matched = True
                break
        if not matched:
            possible = False
            break

    if possible:
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

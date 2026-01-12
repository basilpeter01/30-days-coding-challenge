'''
Day-29
EASY
Accepted
61/61 test cases passed
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    def is_leap_julian(y):
        return y % 4 == 0

    def is_leap_gregorian(y):
        return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

    is_leap = False
    if year < 1918:
        is_leap = is_leap_julian(year)
    elif year > 1918:
        is_leap = is_leap_gregorian(year)

    day = 0
    if year == 1918:
        day = 26
    elif is_leap:
        day = 12
    else:
        day = 13

    month = "09"

    return f"{day:02d}.{month}.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

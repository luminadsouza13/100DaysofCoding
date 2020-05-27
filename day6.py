#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    # Write your code here
    flag=0
    large=0;
    substring=0;
    for i in range(0,len(s)):
        print(s[i:k+i])
        for ch in s[i:k+1]:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
                flag=flag + 1
        print(flag)
        if flag > large:
            large=flag
            substring=i;
            flag=0
            print(large,substring)

    if large != 0:
        return s[substring:]
    else:
        return "Not found!"


if __name__ == '__main__':

    s = "azerdii"

    k = 5

    result = findSubstring(s, k)

    print("result :"+result)
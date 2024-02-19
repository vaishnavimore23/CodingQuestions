#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    fb = [0, 1]
    for i in range(2, n):
        fb.append(fb[i - 1] + fb[i - 2])
    i = 0
    add = 0
    while fb[i] < n:
        if fb[i] % 2 == 0:
            add += fb[i]
        i += 1
    print(add)



import sys
import math

n = int(sys.stdin.readline())
data = [map(int,sys.stdin.readline().strip())]

def bubble_sort(a):
    for i in range(n):
        for j in range(n-1, i, -1):
            
## 10 14888 연산자 끼워넣기 ()

from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
nums = list(map(int,input().split()))
calc = list(map(int,input().split()))
# 0: +, 1: -, 2: *, 3: //

def dfs(clist):
    for i in range(n-1):
        stack = []
        clist[i] -= 1
        stack.append(i)
        while stack:
            c = stack.pop()
            



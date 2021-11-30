## 14 1700 멀티탭 스케줄링

from collections import deque
import sys


input = sys.stdin.readline


n, k = map(int,input().split())
tap_full = False
tap = [0] * n
order = deque(list(map(int,input().split())))
min_d = [101, 101]
while len(tap) <= n :
    d = order.popleft()
    cnt = 0
    for next in order :
        if d == next :
           cnt += 1
    if min_d[1] > cnt :
        min_d = [d, cnt]
    tap.append(d)



    for d in order :
        if not tap_full :
            tap.append(d)
    
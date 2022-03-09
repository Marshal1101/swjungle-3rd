## 12 1931 회의실 배정


import sys


input = sys.stdin.readline


n = int(input())
sche = []
for _ in range(n) :
    sche.append(list(map(int,input().split())))

sche.sort(key=lambda x:x[0])
sche.sort(key=lambda x:x[1])

former_end = 0
cnt = 0
for start, end in sche :
    if start >= former_end :
        cnt += 1
        former_end = end
print(cnt)
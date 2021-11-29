## 11 1541 잃어버린 괄호


import sys


input = sys.stdin.readline


a = input().split('-')
num = []
for i in a :
    s = i.split('+')
    cnt = 0
    for j in s :
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)) :
    n -= num[i]
print(n)
## 99 1003 피보나치 함수 (구현: 01)


import sys


input = sys.stdin.readline


T = int(input())
case = []
for _ in range(T) :
    case.append(int(input()))

n = max(case)

zero = [0] * (n+1)
one = [0] * (n+1)

zero[0] = 1
one[1] = 1

def fibo_zero(k) :
    if k == 0 :
        return 1
    if k == 1 :
        return 0
    if zero[k] != 0 :
        return zero[k]
    else :
        zero[k] = fibo_zero(k-1) + fibo_zero(k-2)
        return zero[k]

def fibo_one(k) :
    if k == 0 :
        return 0
    if k == 1 :
        return 1
    if one[k] != 0 :
        return one[k]
    else :
        one[k] = fibo_one(k-1) + fibo_one(k-2)
        return one[k]

for K in case :
    print(fibo_zero(K), fibo_one(K))
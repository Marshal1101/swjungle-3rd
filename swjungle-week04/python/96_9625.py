## 96 9625 BABBA

# 1003 문제와 같음
# A는 0에 해당하고,
# B는 1에 해당한다.

import sys


input = sys.stdin.readline


K = int(input())

adp = [0] * (K+1)
bdp = [0] * (K+1)

def babba_A(k) :
    if k == 0 :
        return 1
    if k == 1 :
        return 0
    if adp[k] > 0 :
        return adp[k]
    else :
        adp[k] = babba_A(k-1) + babba_A(k-2)
        return adp[k]

def babba_B(k) :
    if k == 0 :
        return 0
    if k == 1 :
        return 1
    if bdp[k] > 0 :
        return bdp[k]
    else :
        bdp[k] = babba_B(k-1) + babba_B(k-2)
        return bdp[k]

print(babba_A(K), babba_B(K))
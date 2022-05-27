# 05 1053 가장 긴 증가하는 수열(암기)

import sys


input = sys.stdin.readline


n = int(input())
s = list(map(int,input().split()))
dp = [0] * (n)

for i in range(n) :
    for j in range(i) :
        if s[i] > s[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

## for 두 개;
## i가 앞서면서 뒤에 놓인 배열 값들 모든 j와 비교함
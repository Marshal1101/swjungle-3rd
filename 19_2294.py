## 19 2294 동전2 ()
# 다이내믹 프로그래밍


import sys


input = sys.stdin.readline


n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input().strip()))

dp = [0] * (k+1)
for i in range(1, k+1):
    used = []
    for coin in coins:
        if coin <= i and dp[i - coin] != -1:
            used.append(dp[i-coin])
    if not used:
        dp[i] = -1
    else:
        dp[i] = min(used) + 1

print(dp[k])
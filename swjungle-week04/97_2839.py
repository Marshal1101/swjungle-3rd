## 97 2839 설탕 배달 (구현: 01)


import sys


input = sys.stdin.readline


N = int(input())
init_min = 5001
dp = [init_min] * 5006
dp[0] = 0
for i in range(N+1) :
    dp[i+5] = min(dp[i+5], dp[i] + 1)
    dp[i+3] = min(dp[i+3], dp[i] + 1)
if dp[N] < 5001 :
    print(dp[N])
else :
    print(-1)
## 90 2579 계단 오르기 (참조, 백준 https://www.acmicpc.net/source/15466693)


import sys

n = int(input())

step = []
for _ in range(n):
    a = int(sys.stdin.readline())
    step.append(a)

dp = [0]*(len(step))
dp[0] = step[0]

if n >=2 :
    dp[1] = step[0] + step[1]

    for i in range(2, len(step)):
        dp[i] = max(step[i]+step[i-1]+dp[i-3], step[i]+dp[i-2])

print(dp[n-1])

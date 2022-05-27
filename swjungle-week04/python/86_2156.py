## 86 2156 포도주 시식


import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * n
g = []
for _ in range(n) :
    g.append(int(input()))
dp[0] = g[0]
## 만약 n = 1 인데, dp[1] 설정하면 백준 인덱스 에러
if n > 1 :
    dp[1] = g[0] + g[1]
for i in range(2, n) :
    dp[i] = max(dp[i-1], dp[i-2] + g[i], dp[i-3] + g[i-1] + g[i])
print(dp[n-1])
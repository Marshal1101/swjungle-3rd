## 06 11049 행렬 제곱 순서 (암기)


import sys


input = sys.stdin.readline


n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (n) for _ in range(n)]

for i in range(1, n) :
    for j in range(n-i) :
        x = j + i
        dp[j][x] = 2**32
        for k in range(j, x) :
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + s[j][0] * s[k][1] * s[j][1])
print(dp[0][n-1])

## 행렬 0번부터 n-1까지 n개의 곱을 최소 회수로 계산하는 법
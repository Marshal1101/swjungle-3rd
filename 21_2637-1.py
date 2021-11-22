## 21 2637 장난감 조립 (런타임 에러 (IndexError))
# 다이나믹 프로그래밍 사용

# 그래프 이론
# 위상 정렬
# 다이나믹 프로그래밍

from collections import deque
import sys


input = sys.stdin.readline


n = int(input())
m = int(input())
dp = [[0] * i for i in range(n+1)]
mid_check = []
for _ in range(m):
    end, start, ea = map(int,input().split())
    mid_check.append(end)
    dp[end][start] = ea
mid = min(mid_check)

def DIY(n):
    for _ in range(mid, n+1):
        for i in range(mid, n):
            if dp[n][i] != 0:
                for j in range(i): 
                    if dp[i][j] != 0:
                        dp[n][j] += dp[i][j] * dp[n][i]
                dp[n][i] = 0
    return dp[n]

DIY(n)
for k in range(n):
    if dp[n][k] != 0:
        print(f'{k} {dp[n][k]}')
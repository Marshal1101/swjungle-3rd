## 89 1932 정수 삼각형 (구현: 01)


import sys


input = sys.stdin.readline


n = int(input())
dp = []
for _ in range(n) :
    dp.append(list(map(int,input().split())))

# print(tr)    
# print(dp)
for i in range(1, n) :
    for j in range(i+1) :
        if j == 0 :
            dp[i][0] = dp[i][0] + dp[i-1][0]
        elif j == i :
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
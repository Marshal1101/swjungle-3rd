## 03 9084 동전 ()


import sys


input = sys.stdin.readline

dp = [0 for _ in range(10001)]
t = int(input())
for _ in range(t) : 
    n = int(input())
    lst = list(map(int,input().split()))
    m = int(input())
    if lst[0] == 1:
        dp = [1 for _ in range(10001)]
        for k in lst :
            if k == 1 :
                continue
            for i in range(1, m+1) :
                if i - k >= 0 :
                    dp[i] += dp[i-k]
        print(dp[m])
    else :
        dp = [0 for _ in range(10001)]
        dp[0] = 1
        for k in lst :
            for i in range(1, m+1) :
                if i - k >= 0 :
                    dp[i] += dp[i-k]
        print(dp[m])
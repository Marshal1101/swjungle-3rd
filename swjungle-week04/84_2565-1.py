## 84 2565 전깃줄 (참조, https://pacific-ocean.tistory.com/159)


import sys
input = sys.stdin.readline


n = int(input())
w = []
w_b = []
dp = [0 for i in range(n)]
for _ in range(n) :
    w.append(list(map(int,input().split())))
w.sort(key=lambda x:x[0])
for i in range(n) :
    w_b.append(w[i][1])
for i in range(n) :
    for j in range(i) :
        if w_b[i] > w_b[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))
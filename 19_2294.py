## 19 2294 동전2 (구현: 01)
# 다이내믹 프로그래밍


import sys


input = sys.stdin.readline


n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input().strip()))

# dp 메모리: i값를 만들기 위해 사용한 동전 수를 저장한다.
dp = [0] * (k+1)

for i in range(1, k+1):
    used = []
    for coin in coins:
        if coin <= i and dp[i - coin] != -1:
            used.append(dp[i-coin])
    # i - coin 값을 만들 수 없었다면 i값을 만드는 것도 불가능: -1로 표시
    if not used:
        dp[i] = -1
    # i - coin 값을 만들었다면 i값은 coin값 한 개만 추가하면 가능
    # 그리고 이것이 점화식: dp[i] = min(i-coin을 만들었던 모든 dp[i-coin]) + 1
    else:
        dp[i] = min(used) + 1

print(dp[k])
## 09 2253 점프 (참조, https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-2253-%EC%A0%90%ED%94%84-Python)


import sys
input = sys.stdin.readline

import sys
N, M = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))
for i in range(2, N + 1):
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))



# 이때 int((2 * N) ** 0.5) + 1는
# 1부터 속도가 끊임없이 1씩 증가하며 점프할 때
# N에 도달했을 때의 속도의 근사값이다.
# 즉 첫째항이 1이고 공차가 1인 등차수열에서
# 수열의 합이 N이 될 때 마지막 항의 값의 근사값이고
# 아래와 같은 과정을 거쳐 이 값을 얻을 수 있다.

# K * (K + 1) / 2 = N
# K ** 2 + K = 2N 
# K = (2N - K) ** 0.5 < 2N ** 0.5
# 그리고 i를 현재 위치, j를 현재 속도라고 했을 때
# dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
# 이라는 점화식을 얻을 수 있다.
# 이 점화식은 i라는 점에 j의 속도로 도달했을 때의 최소 점프횟수는
# i - j의 위치에 각각 j - 1, j, j + 1의 속도로 도달했을 때의
# 최소 점프횟수 + 1이라는 뜻이다.
# j - 1, j, j + 1의 속도에서 각각 +1, +0, -1을 했을 때
# j만큼 점프할 수 있기 때문에 i - j에서 i로 갈 수 있기 때문이다.
# 그리고 이 때 j의 최대값은 int((2 * i) ** 0.5) + 1이다.
# 이는 앞에서 설명했듯이 1에서부터 속도가 끊임없이 증가하며 점프할 때
# i에 도달했을 때의 속도의 근사값이다.
# 위 내용을 이해했다면 어려움 없이 문제를 해결할 수 있을 것이다.
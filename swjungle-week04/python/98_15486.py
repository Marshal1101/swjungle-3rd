## 98 15486 퇴사 2 (구현: 01)


import sys


input = sys.stdin.readline

N = int(input())
T, P = [], []
for _  in range(N) :
    work, pay = map(int,input().split())
    T.append(work)
    P.append(pay)

dp = [0] * (N+1)

for i in range(N) :
    # 퇴사 전까지 가능한 일인지 체크한 뒤,
    if T[i] <= N - i :
        # 오늘(i) 내가 이 일을 하면 걸리는 시간(T[i]) 지나서,
        # 그날(i+T[i])에 예상되는 소득 dp[i+T[i]]이 있었어
        # >>근데 어제까지(아마도 i-1까지) 예상해본 소득이야<<
        # 오늘까지 번 돈 dp[i]에 오늘 이거 일을 하면 P[i]
        # dp[i] + P[i]인데, 만약에 이 돈이 더 크면
        # i+T[i] 날에 생길 기대 소득을 갱신해야지. 
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])

    # 내일(i+1) 기대소득 dp은 과거 언젠가 예상했던 거고,
    # 오늘 dp[i] 이것은 확정된 거잖아. 오늘 dp[i]이 크다면,
    # 갱신해야지
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])

# 현실에서는 어떤 선택을 하면 되돌릴 수 없고, 또다른 선택을 했던 나는 없지만,
# 경우의 수가 동시적인(?) 컴퓨터에서는 언제나 최적의 선택이 발견되면,
# 평행우주 건너가듯 지금 여기 i에서 미래i+n와 과거i-n를 수정한다.


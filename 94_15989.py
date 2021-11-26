## 94 15989 1,2,3 더하기 4


import sys


input = sys.stdin.readline


t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])


# 식을 하나로만 세우려고 해서 오히려 어려웠던 것 같다.
# 관점을 조금 바꾸면 풀이 방법이 보이는 문제다.

# 우선, 1만 써서 합을 나타내는 방법 1가지씩은 모두 가지고 있으므로
# dp 테이블을 1로 초기화해준다. 그리고 2가 추가되는 경우
# dp[i] = dp[i] + dp[i - 2]와 
# 3이 추가되는 경우
# dp[i] = dp[i] + dp[i - 3]를 한번씩 더 갱신해주면 된다.
## 04 9251 LCS(Longest Common Subsequence) (참조, https://pacific-ocean.tistory.com/160)


import sys


input = sys.stdin.readline


m = list(input())
n = list(input())
m_len = len(m)
n_len = len(n)
dp = [[0] * (n_len + 1) for i in range(m_len + 1)]
for i in range(m_len):
    for j in range(n_len):
        if m[i] == n[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[m_len][n_len])


# 서로 비교해나가며 같다면 왼쪽대각선 숫자에 +1한 값을 넣음.
# 같지 않다면 왼쪽과 위를 비교해 큰 값을 넣음.
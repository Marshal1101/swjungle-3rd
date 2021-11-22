## 10 14888 연산자 끼워넣기 (참조)
# dfs 백트래킹
# 백트래킹? 놀랍다. 값을 넘겨주며 연산하고 결과를 재귀


import sys
input = sys.stdin.readline


def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt + 1, result + s[cnt], p - 1, m, mul, div)
    if m:
        dfs(cnt + 1, result - s[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * s[cnt], p, m, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // s[cnt]) if result < 0 else result // s[cnt], p, m, mul, div - 1)


n = int(input())
s = list(map(int, input().split()))
op = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1, s[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)
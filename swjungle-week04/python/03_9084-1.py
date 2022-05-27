## 03 9084 동전 (참조, 백준 빠른 풀이)


import sys; input = lambda: sys.stdin.readline().rstrip()

def solve(coins, m) :
    v = [1] + [0 for i in range(m)]
    for c in coins :
        for i in range(c, len(v)) :
            v[i] += v[i-c]
    return v[m]

tc = int(input())
for t in range(tc) :
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    print(solve(c, m))
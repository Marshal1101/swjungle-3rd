## 05 12865 평범한 배낭 (참조, 백준 빠른 풀이 https://www.acmicpc.net/source/32377925)


import sys

input = sys.stdin.readline


def sol12865():
    n, k = map(int, input().split())
    dp = {0:0}
    for i in range(n):
        w, v = map(int, input().split())
        u = {}
        for value, weight in dp.items():
            nw, nv = w + weight, v + value
            if nw < dp.get(nv, k+1):
                print(dp.get(nv, k+1))
                u[nv] = nw
        dp.update(u)
    return max(dp.keys())


if __name__ == '__main__':
    print(sol12865())
            
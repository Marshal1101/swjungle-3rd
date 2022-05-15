## 11 2573 빙산 (참조, 백준 빠른 풀이)
# DFS 사용
# 딕셔너리 활용!!! {}, enumerate, iter

# 구현
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색

import sys

N, M = map(int, sys.stdin.readline().split())

ice_h = {}
ice_b = {}
for i, row in enumerate(sys.stdin.readlines()):
    for j, n in enumerate(map(int, row.split())):
        if n:
            ice_h[(i, j)] = n
            ice_b[(i, j)] = 4
            if (i, j-1) in ice_h:
                ice_b[(i, j)] -= 1
                ice_b[(i, j-1)] -= 1
            if (i-1, j) in ice_h:
                ice_b[(i, j)] -= 1
                ice_b[(i-1, j)] -= 1

def check():
    it = next(iter(ice_h))
    stack = [it]
    visited = set(stack)
    while stack:
        i, j = stack.pop()
        for coor in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if coor in ice_h and coor not in visited:
                stack.append(coor)
                visited.add(coor)
    return len(ice_h) != len(visited)

def update():
    del_items = []
    for i in ice_h:
        if ice_h[i] > ice_b[i]:
            ice_h[i] -= ice_b[i]
        else:
            del_items.append(i)
    
    for i, j in del_items:
        for coor in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if coor in ice_b:
                ice_b[coor] += 1
        del ice_b[(i, j)]
        del ice_h[(i, j)]

def sol(ice_h, ice_b):
    year = 0
    while 1:
        year += 1
        update()
        if len(ice_h) == 0:
            return 0
        if check():
            return year

print(sol(ice_h, ice_b))
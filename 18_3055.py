## 18 3055 탈출 (런타임 에러 (NameError))
# BFS

import sys
input = sys.stdin.readline


r, c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            end = (i, j)
        elif graph[i][j] == '*':
            water = (i, j)
        elif graph[i][j] == 'S':
            start = (i, j)
        elif graph[i][j] == 'X':
            graph[i][j] = '*'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    time = 0
    find = False
    wq = [water]
    sq = [start]
    while sq:
        time += 1
        nwq = []
        for x, y in wq:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                    nwq.append((nx, ny))
                    graph[nx][ny] = '*'
        wq = nwq

        nsq = []
        check = False
        for x, y in sq:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (nx, ny) == end:
                    check = True
                    break
                if 0<= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                    nsq.append((nx, ny))
                    graph[nx][ny] = '*'

        if check:
            find = True
            break
        sq = nsq
    
    return time if find else 'KAKTUS'

print(BFS())
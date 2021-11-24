## 18 3055 탈출 (메모리 초과)
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

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS():
    time = 0
    find = False
    wq = [water]
    sq = [start]
    while sq:
        nwq = []
        for i, j in wq:
            for k in range(4):
                ny = i + di[k]
                nx = j + dj[k]
                if 0<= ny < r and 0 <= nx < c and graph[ny][nx] == '.':
                    nwq.append((nx, ny))
                    graph[nx][ny] = '*'
        wq = nwq
        nsq = []
        check = False
        for i, j in sq:
            for k in range(4):
                ny = i + di[k]
                nx = j + dj[k]
                if (ny, nx) == end:
                    check = True
                    break
                if 0 <= ny < r and 0 <= nx < c and (graph[ny][nx] == '.' or graph[ny][nx] == 'D'):
                    nsq.append((ny, nx))
                    graph[ny][nx] = '*'

        if check:
            find = True
            break
        sq = nsq
        time += 1    
    return time if find else 'KAKTUS'

print(BFS())
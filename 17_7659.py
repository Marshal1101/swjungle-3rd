## 17 7659 토마토 (구현: 01) 그런데 내가 짠 건 왜 time에서 -1 해줘야 나오는지 모르겠다.
# BFS 사용

# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색


import sys


input = sys.stdin.readline

# box[h][n][m]
m, n, h = map(int,input().split())
box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int,input().split())))


def BFS():
    time = 0
    all = m * n * h
    empty = 0
    red = 0
    rq = []
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 1:
                    red += 1
                    rq.append((z, y, x))
                elif box[z][y][x] == -1:
                    box[z][y][x] = 1
                    empty += 1

    green = all - empty - red
    if all == red + empty:
        return 0

    cnt = 0
    while rq:
        nrq = []
        for z, y, x in rq:
            if z - 1 >= 0 and box[z-1][y][x] == 0:
                box[z-1][y][x] = 1
                cnt += 1
                nrq.append((z-1, y, x))
            if z + 1 < h and box[z+1][y][x] == 0:
                box[z+1][y][x] = 1
                cnt += 1
                nrq.append((z+1, y, x))
            if y - 1 >= 0 and box[z][y-1][x] == 0:
                box[z][y-1][x] = 1
                cnt += 1
                nrq.append((z, y-1, x))
            if y + 1 < n and box[z][y+1][x] == 0:
                box[z][y+1][x] = 1
                cnt += 1
                nrq.append((z, y+1, x))
            if x - 1 >= 0 and box[z][y][x-1] == 0:
                box[z][y][x-1] = 1
                cnt += 1
                nrq.append((z, y, x-1))
            if x + 1 < m and box[z][y][x+1] == 0:
                box[z][y][x+1] = 1
                cnt += 1
                nrq.append((z, y, x+1))
        rq = nrq
        time += 1

    if cnt == green:
        return time - 1
    else:
        return -1

print(BFS())
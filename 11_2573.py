## 11 2573 빙산 ( )
# DFS 사용

# 구현
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색

import sys


input = sys.stdin.readline


n, m = map(int,input().split())
world = []
for _ in range(n):
    world.append(list(map(int,input().split())))

check = [[False for _ in range(m)] for _ in range(n)]
def DFS(x, y):
    if check[x][y] == True:
        return 0
    stack = [(x, y)]
    check[x][y] = True
    while stack:
        x, y = stack.pop()
        if x - 1 >= 0:
            if world[x-1][y] == 0: 
                if not check[x-1][y]:
                    world[x][y] -= 1
            else:
                if not check[x-1][y]:
                    check[x-1][y] = True
                    stack.append((x-1, y))
        if x + 1 < n:
            if world[x+1][y] == 0:
                if not check[x+1][y]:
                    world[x][y] -= 1
            else:
                if not check[x+1][y]:
                    check[x+1][y] = True
                    stack.append((x+1, y))
        if y - 1 >= 0:
            if world[x][y-1] == 0:
                if not check[x][y-1]:
                    world[x][y] -= 1
            else:
                if not check[x][y-1]:
                    check[x][y-1] = True
                    stack.append((x, y-1))
        if y + 1 < m:
            if world[x][y+1] == 0:
                if not check[x][y+1]:
                    world[x][y] -= 1
            else:
                if not check[x][y+1]:
                    check[x][y+1] = True
                    stack.append((x, y+1))
        if world[x][y] > 0:
            new_world.append((x, y))
            world[x][y] = 0
    return 1

end = False
year = 1
while True:
    count = 0
    new_world = []
    for i in range(1, n-1):
        if count > 1:
            end = True
            break
        for j in range(1, m-1):
            if world[i][j] != 0:
                count += DFS(i, j)
                if count > 1:
                    end = True
                    break
    else:
        if new_world == []:
            print(0)
            break
        year += 1
        check = [[[False] for _ in range(m)] for _ in range(n)]
        new_world = []
    if end == True:
        print(year)
        break
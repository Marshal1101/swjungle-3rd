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
def DFS(y, x):
    if check[y][x] == True:
        return 0
    stack = [(y, x)]
    check[y][x] = True
    while stack:
        y, x = stack.pop()
        if x - 1 >= 0 and not check[y][x-1]:
            if world[y][x-1] == 0: 
                world[y][x] -= 1
            else:
                check[y][x-1] = True
                stack.append((y, x-1))
        if x + 1 < m and not check[y][x+1]:
            if world[y][x+1] == 0:
                world[y][x] -= 1
            else:
                check[y][x+1] = True
                stack.append((y, x+1))
        if y - 1 >= 0 and not check[y-1][x]:
            if world[y-1][x] == 0:
                world[y][x] -= 1
            else:
                check[y-1][x] = True
                stack.append((y-1, x))
        if y + 1 < n and not check[y+1][x]:
            if world[y+1][x] == 0:
                world[y][x] -= 1
            else:
                check[y+1][x] = True
                stack.append((y+1, x))
        if world[y][x] > 0:
            new_world.append((y, x))
        else:
            world[y][x] = 0
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
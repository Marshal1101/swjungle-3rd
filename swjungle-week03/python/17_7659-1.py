## 17 7659 토마토 (참조, 백준 빠른 풀이)
# BFS 사용

# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색


from sys import stdin

def solution():
    l = stdin.readlines()
    n, m, h = map(int, l.pop(0).split())
    board = list(zip(*[iter(list(map(int, ll.split())) for ll in l)] * m))
    cnt = 0
    tomatoes = []
    depth = -1

    for k in range(h):
        for i in range(m):
            for j in range(n):
                if board[k][i][j] == 0:
                    cnt += 1
                elif board[k][i][j] == 1:
                    tomatoes.append((k, i, j))

    while tomatoes:
        depth += 1
        temp = []
        for k, i, j in tomatoes:
            if k > 0 and board[k-1][i][j] == 0:
                board[k-1][i][j] = 1
                temp.append((k-1,i,j))
            if i > 0 and board[k][i-1][j] == 0:
                board[k][i-1][j] = 1
                temp.append((k,i-1,j))
            if j > 0 and board[k][i][j-1] == 0:
                board[k][i][j-1] = 1
                temp.append((k,i,j-1))
            if k < h-1 and board[k+1][i][j] == 0:
                board[k+1][i][j] = 1
                temp.append((k+1,i,j))
            if i < m-1 and board[k][i+1][j] == 0:
                board[k][i+1][j] = 1
                temp.append((k,i+1,j))
            if j < n-1 and board[k][i][j+1] == 0:
                board[k][i][j+1] = 1
                temp.append((k,i,j+1))
        cnt -= len(temp)
        tomatoes = temp

    return -1 if cnt else depth
                
print(solution())
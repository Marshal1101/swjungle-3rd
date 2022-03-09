## 18 3055 탈출 (참조, 백준 빠른 풀이)

import sys

input = sys.stdin.readline


def sol3055():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    wq = []
    goal_r, goal_c = 0, 0
    start_r, start_c = 0, 0
    for r in range(n):
        for c in range(m):
            if board[r][c] == '*':
                wq.append((r, c))
            elif board[r][c] == 'D':
                goal_r, goal_c = r, c
            elif board[r][c] == 'S':
                start_r, start_c = r, c
            elif board[r][c] == 'X':
                board[r][c] = '*'

    q = [(start_r, start_c)]
    board[start_r][start_c] = '*'
    time = 0
    find = False
    while q:
        # 1. 물이 찬다
        nwq = []
        for r, c in wq:
            if r - 1 >= 0 and board[r - 1][c] == '.':
                board[r - 1][c] = '*'
                nwq.append((r - 1, c))
            if r + 1 < n and board[r + 1][c] == '.':
                board[r + 1][c] = '*'
                nwq.append((r + 1, c))
            if c - 1 >= 0 and board[r][c - 1] == '.':
                board[r][c - 1] = '*'
                nwq.append((r, c - 1))
            if c + 1 < m and board[r][c + 1] == '.':
                board[r][c + 1] = '*'
                nwq.append((r, c + 1))
        wq = nwq

        # 2. 고슴도치가 이동한다
        nq = []
        check = False
        for r, c in q:
            if r == goal_r and c == goal_c:
                check = True
                break
            if r - 1 >= 0 and board[r - 1][c] != '*':
                board[r - 1][c] = '*'
                nq.append((r - 1, c))
            if r + 1 < n and board[r + 1][c] != '*':
                board[r + 1][c] = '*'
                nq.append((r + 1, c))
            if c - 1 >= 0 and board[r][c - 1] != '*':
                board[r][c - 1] = '*'
                nq.append((r, c - 1))
            if c + 1 < m and board[r][c + 1] != '*':
                board[r][c + 1] = '*'
                nq.append((r, c + 1))

        if check:
            find = True
            break
        q = nq
        time += 1

    return time if find else 'KAKTUS'


if __name__ == '__main__':
    print(sol3055())
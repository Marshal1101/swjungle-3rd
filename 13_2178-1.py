## 13 2178 미로 탐색 (참조)

# 방문리스트 없이도 구현가능해서 놀랐다.
# 아, 그 이유는 이동하면서 지나온 길을
# "1" 에서 이동회수로 바꾸었기 때문에
# 돌아가는 경우가 발생하지 않았다.


n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
print(s[n - 1][m - 1])
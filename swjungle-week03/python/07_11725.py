## 07 11725 트리의 부모 찾기 (구현: 01)
## dfs 재귀함수 재귀 제한 해제 200000

# 알고리즘 분류
# 그래프 이론
# 그래프 탐색
# 트리
# 너비 우선 탐색
# 깊이 우선 탐색

# 문제
# 루트 없는 트리가 주어진다. 
# 이때, 트리의 루트를 1이라고 정했을 때, 
# 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.


import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n = int(input())
vertex = [[] for _ in range(n+1)]
for i in range(n-1):
    v1, v2 = map(int,input().split())
    vertex[v1].append(v2)
    vertex[v2].append(v1)

visited = [[False, 0] for _ in range(n+1)]

def dfs(vertex, start, visited):
    visited[start][0] = [True]
    for v in vertex[start]:
        if visited[v][0] == False:
            visited[v][1] = start
            dfs(vertex, v, visited)
    
dfs(vertex, 1, visited)
for i in range(2, n+1):
    print(visited[i][1])
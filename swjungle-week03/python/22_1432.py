## 22 1432 그래프 수정 (틀림)
# 위상 정렬 사용

# 그래프 이론
# 플로이드–와샬
# 위상 정렬


from collections import deque
import sys


input = sys.stdin.readline


# 자료구조
# 인접리스트
# 자식 수 = 진입차수
n = int(input())
data = []
for _ in range(n) :
    data.append(list(map(int,input().strip())))

graph = [[] for _ in range(n+1)]
child = [ 0 for i in range(n+1)]

for i in range(n) :
    for j in range(n) :
        if data[i][j] :
            graph[i+1].append(j+1)
            child[j+1] += 1

# 위상 정렬 함수
def topology_sort() :
    result = []
    q = deque()
    # 처음 시작 시 진입차수가 0인 노드를 찾아서 큐에 삽입
    for i in range(1, n+1) :
        if child[i] == 0:
            q.append(i)
    if not q :
        print(-1)
        return
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 꺼낼 때 그것이 곧 순서라서 결과에 보낸다.
        now = q.popleft()
        result.append(now)
        # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
            child[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if child[i] == 0 :
                q.append(i)

    new_order = [0] * (n+1)
    for i in range(n) :
        new_order[result[i]] = i+1

    if result != new_order :
            print(*new_order[1:], end=' ')
    else:
        print(-1)


topology_sort()
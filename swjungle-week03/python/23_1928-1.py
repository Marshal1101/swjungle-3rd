## 23 1948 임계경로 (참조, https://uneducatedjungler.tistory.com/85?category=970202)
# DFS 2개 사용

# 그래프 이론
# 그래프 탐색
# 위상 정렬


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


Vn = int(input())
En = int(input())
V = {}
child = [0 for i in range(Vn + 1)]
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2, c = map(int, input().split())
    V[v1].append([v2, c])
    child[v1] = child[v1] + 1
start, end = map(int, input().split())
 
D = [0 for i in range(Vn + 1)]
def DFS1(now) : 
    for next, cost in V[now] : 
        if child[next] == 0 : 
            child[now] = child[now] - 1
            D[now] = max(D[now], D[next] + cost)
        else : 
            child[now] = child[now] - 1
            DFS1(next)
    for next, cost in V[now] : 
        D[now] = max(D[now], D[next] + cost)
DFS1(start)
print(D[start])
 
gone = [False for i in range(Vn + 1)]
count = 0
def DFS2(now) : 
    global count
    for next, cost in V[now] : 
        if D[now]- D[next] == cost : 
            count = count + 1
            if not gone[next] : 
                gone[next] = True
                DFS2(next)
DFS2(start)
print(count)





# line 5 ~ 15

# 인풋받은 정보들을 기록한다. 
# 자식이 0개인 노드부터(end점부터) end와의 최장거리를 기록할 것이기 때문에, 
# 각 점의 자식 수를 기록하는 리스트 child도 작성한다.

 

# line 17 ~ 25

# end와의 최장거리를 기록하는 리스트 D를 만들고, 
# 현재점 now에서 갈 수 있는 next들로 분기하는 DFS를 정의한다.

# next의 child가 0이라면
# D[now]를 D[next] + cost로 갱신하고, 
# now의 child를 하나 줄이며 재귀를 마친다.

# next의 child가 0이 아니라면, 
# next에서 DFS를 다시 실행하여 재귀한다.

 

# line 26 ~ 29

# line 25의 재귀함수 이후가 실행될 때에는,
# next에 대해 DFS가 다 돌았으니 now의 child는 0이 되었다. (후위 순회)

# 이때 D[next] + cost들의 max값을 구해
# 그것으로 D[now]의 값을 갱신하며 재귀를 마친다.

# 이렇게 정의한 DFS를 start점에서 실행하면,
# D에는 각 점의 end값까지의 최장거리가 기록되어있다.

# D[start]를 출력한다.

 

# line 31 ~ 40

# 작성된 D를 이용하여 DFS를 하나 더 정의한다.

# 작성된 연결 정보 V[now]에 기록된 now와 next의 연결 비용 cost가 
# D[now] - D[next]와 같다면(line 36)

# 이 경로는 최장경로에 포함되었으며, 
# 지금 DFS의 순회가 최장경로를 제대로 따라가고 있다는 것이다.

# 그러므로 count를 더해주고 next에서도 DFS를 실행한다. 
# 이때 중복실행을 막기 위해 방문 정보 gone을 기록한다.

# 만약 line 36에서 다르다면, 
# 이 경로는 최장경로와는 다른 길이므로 더이상 아무것도 실행하지 않고 재귀를 마친다.

# 위의 기능을 하는 DFS를 start점에서 실행한 뒤
# count 값이 최장 경로들에 포함된 경로의 갯수이다.
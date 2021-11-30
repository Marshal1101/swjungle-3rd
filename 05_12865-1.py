## 05 12865 평범한 배낭 (참조, https://uneducatedjungler.tistory.com/102?category=970202)


import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
C = []
for i in range(n) : 
    C.append(list(map(int, input().split())))
f = [[0 for i in range(k + 1)] for i in range(n)]
 
for i in range(n) : 
    w, v = C[i][0], C[i][1]
    for j in range(1, k + 1) : 
        if j >= w : 
            f[i][j] = max(f[i-1][j], f[i-1][j - w] + v)
        else : 
            f[i][j] = f[i-1][j]
print(f[n-1][k])


# n개의 물건으로 무게 k의 가방을 쌌을때 최대 가치를 f(n, k)라고 하자.
# f(n, k)를 구성하는데에는 n번째 물건(무게 w 가치 v)이 필요할 수도, 필요 없을 수도 있다.
# n이 필요 없다면 f(n, k)는 n-1까지로 구성된 가방의 최대 가치와 같다.
# f(n, k) = f(n-1, k)
# n이 필요하다면 아직 n을 넣지 않은 가방의 상태를 고려해본다.
# 완성품의 무게는 k이므로, n을 넣기 전 이 가방의 무게는 k-w이며,여기에 가치 v의 n을 넣은것이 완성품이다.
# f(n, k) = f(n-1, k-w) + v
# 위의 두 후보 중에서 큰 것이 f(n, k)가 되므로 점화식은 아래와 같이 표현된다.
# f(n, k) = max(f(n-1, k), f(n-1, k-w) + v)
# 점화식의 변수가 2개이므로, 2차원 DP table을 작성하여 점화식대로 값을 채워나간 뒤 table의 끝점을 출력한다.
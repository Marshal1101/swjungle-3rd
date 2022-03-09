## 21 2637 장난감 조립 (참조, 백준 빠른 풀이 https://www.acmicpc.net/source/10685524)
# 트리 사용
# 클래스 사용, 딕셔너리 사용

# 그래프 이론
# 위상 정렬
# 다이나믹 프로그래밍

# 초기화
class Node :
    def __init__(self, name) :
        self.name = name
        self.chd = {}
        self.nds = {}

    # 구성
    def con(self, node, n) :
        self.chd[node] = n

    # 
    def needs(self) :
        if not self.chd :
            return {self.name: 1}
        if self.nds :
            return self.nds
        for ch, n in self.chd.items() :
            for i, m in ch.needs().items() :
                self.nds[i] = self.nds.get(i, 0) + m*n
        return self.nds


class Techtree :
    def __init__(self, n) :
        self.nodes = [Node(i) for i in range(n+1)]
    def con(self, fr, to, n) :
        self.nodes[fr].con(self.nodes[to], n)
    def needs(self, k) :
        return self.nodes[k].needs()


n = int(input())
m = int(input())
tree = Techtree(n)
for i in range(m) :
    x,y,k = map(int, input().split())
    tree.con(x, y, k)
res = tree.needs(n)
for i in range(n+1) :
    if i in res :
        print(i, res[i])

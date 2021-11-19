## 02 5639 이진 검색 트리 (완료)
## 함수 안에 for ~ else 구성해서 return하면 무한루프 걸렸었다.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def changer(list):
    length = len(list)
    if length <= 1:
        return list
    for i in range(1, length):
        if list[0] < list[i]:
            return changer(list[1:i]) + changer(list[i:]) + [list[0]]
    return changer(list[1:]) + [list[0]]

trees = changer(tree)
for n in trees:
    print(n)
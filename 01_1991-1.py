## 01 1991 트리 순회 (참조: 01)
## 노드 특성, 딕셔너리 특성 이해 필요

# 문제
# 이진 트리를 입력받아 
# 전위 순회(preorder traversal), 
# 중위 순회(inorder traversal), 
# 후위 순회(postorder traversal)
# 결과를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
# 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회
    print(node.key, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):  # 중위 순회
    if node.left != '.':
        inorder(tree[node.left])
    print(node.key, end='')
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):  # 후위 순회
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.key, end='')


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(key=node, left=left, right=right)


    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
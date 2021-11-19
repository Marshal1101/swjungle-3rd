## 01 1991 트리 순회 (참조)
## 노드 특성, 딕셔너리 특성 이해 필요

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
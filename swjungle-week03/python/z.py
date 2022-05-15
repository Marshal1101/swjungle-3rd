## 이진 검색 트리 클래스 (참조)

from __future__ import annotations
from typing import Any, Type
import sys

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, left: Node = None,
                 right: Node = None):
        """생성자"""
        self.key = key      # 키
        self.left = left    # 왼쪽 포인터(왼쪽 자식 참조)
        self.right = right  # 오른쪽 포인터(오른쪽 자식 참조)

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None  # 루트

    def postorder(self, node):  # 후위 순회
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right)
        print(node.key)

    def add(self, key: Any) -> bool:
        """키가 key인 노드를 삽입"""

        def add_node(node: Node, key: Any) -> None:
            """node를 루트로 하는 서브 트리에 키가 key인 노드를 삽입"""
            if key == node.key:
                return False  # key가 이진검색트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, None, None)
                else:
                    add_node(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key, None, None)
                else:
                    add_node(node.right, key)
            return True

        if self.root is None:
            self.root = Node(key, None, None)
            return True
        else:
            return add_node(self.root, key)


if __name__ == "__main__":
    s = BinarySearchTree()
    n = 10000
    for i in range(n):
        try:
            s.add(sys.stdin.readline().strip())
        except:
            break

    s.postorder(s.root)    
    
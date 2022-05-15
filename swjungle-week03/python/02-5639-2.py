## 02 5639 이진 검색 트리 (참조: 01)

# 문제

# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 
# 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

# 입력
# 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 
# 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

# 출력
# 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def getPostorder(nums):
    length = len(nums)

    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]

    return getPostorder(nums[1:]) + [nums[0]]


if __name__ == '__main__':
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break

    nums = getPostorder(nums)
    for n in nums:
        print(n)
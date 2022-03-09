## 13 1946 신입사원
# (참조, https://uneducatedjungler.tistory.com/109?category=970202)


import sys
input = sys.stdin.readline
 
testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    l = []
    for i in range(n) : 
        l.append(list(map(int, input().split())))
    l.sort()
    top = sys.maxsize
    count = 0
    for a, b in l : 
        if b < top : 
            count = count + 1
            top = b
    print(count)


# IDEA
# 등수에는 중복이 없다.
# 서류심사 성적 ([0]) 순으로 정렬하면 각 인풋의 [0]은 1, 2, 3, 4, ...가 된다.
# 즉 모든 원소는 자기보다 앞에있는 원소들에 비해 서류심사 성적이 뒤지게 되고, 면접성적([1])만 고려하면 된다.
# 리스트의 앞에서부터 for문을 돌려 top(=min)보다 면접성적이 좋다면(=작다면) 거름당하지 않는다.
# count를 +1하고 top를 갱신한다.
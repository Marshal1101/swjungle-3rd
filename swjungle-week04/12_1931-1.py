## 12 1931 회의실 배정 (백준, 빠른 풀이)

# 최대 회의 갯수 찾기
# 회의 시작시간이 겹치는 것은 전부 제일 작은걸로 갱신, (제일 작은 값으로 하니까 어떤 경우에 대하여 카운트를 못하는 경우가 발생하여 그냥 저장하는 방식으로 했음)
# 시작시간 키값, 도착시간 밸류로 딕셔너리에 저장할 것임
# 회의 시작 시간 순으로 정렬하여 출력 (keys 만 sort 하여 dic[key] 방식으로 불러올 것임)
# 현재 회의의 종료시간 저장 그리고 종료시간보다 늦은 시작 시간인 녀석이 나오면 종료시간 갱신 및 카운트 더하기 일
# 종료시간보다 종료시간이 더 이른 녀석이 나오면 종료시간 갱신, 카운트는 유지

"""
2번 항목에 대한 반례
3
1 5
2 3
2 2
answer: 2
output: 1
"""

import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    dic = {}
    for _ in range(N):
        start, end = map(int, input().split())
        if dic.get(start):
            dic[start].append(end)  # min(dic.get(start, float('inf')), end)
        else:
            dic[start] = [end]
    
    for k in dic.keys():
        dic[k].sort()
        
    keys = sorted(dic.keys())
    end = 0
    count = 0
    for key in keys:
        for e in dic[key]:
            if e < end:
                end = e
            elif key >= end:
                count += 1
                end = e

    print(count)


solve()

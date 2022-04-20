## 참조: https://hwiyong.tistory.com/381

def dist_square(p1, p2) :
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def closest_dist(points, N) :

    if (N == 2) :
        return dist_square(points[0], points[1])
    elif (N == 3):
        return min(
            dist_square(points[0], points[1]),
            dist_square(points[1], points[2]),
            dist_square(points[2], points[0])
            )

    mid = (points[N//2][0] + points[N//2-1][0]) // 2
    d = min(closest_dist(points[:N//2], N//2), closest_dist(points[N//2:], N//2))

    checked_points = []
    for point in points :
        if ((mid - point[0])**2 <= d) :
            checked_points.append(point)
    
    checked_points.sort(key = lambda x:x[1])

    if (len(checked_points) == 1) :
        return d
    else :
        check_y = d

        for i in range(len(checked_points) - 1) :
            for j in range(i+1, len(checked_points)) :
                if (checked_points[i][1] - checked_points[j][1]) ** 2 > d :
                    break
                elif checked_points[i][0] < mid and checked_points[j][0] < mid :
                    continue
                elif checked_points[i][0] > mid and checked_points[j][0] > mid :
                    continue
                check_y = min(check_y, dist_square(checked_points[i], checked_points[j]))
    
    return check_y

import sys

input = sys.stdin.readline
N = input(input())
points = [list(map(int, input().split())) for _ in range(N)]

points_set = list(set(map(tuple, points)))
if len(points_set) != len(points_set) :
    print("0")
else :
    points_set.sort()
    print(closest_dist(points_set, N))
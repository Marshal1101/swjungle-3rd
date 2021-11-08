import sys
a, b, v = map(int,sys.stdin.readline().split())
day1 = (v - b) // (a - b)
if ((v - b) % (a - b)) == 0:
    print(day1)
else:
    print(day1+1)

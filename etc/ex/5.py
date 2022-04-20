abillities, k = [7, 6, 8, 9, 10], 1

answer = 0
arr = sorted(abillities, reverse=True)
if len(abillities)%2 == 1: arr.append(0)

diff = []
for i in range(0,len(arr),2):
    diff.append(arr[i]-arr[i+1])

for i in range(1, len(arr), 2):
    answer += arr[i]

diff.sort(reverse=True)
for i in range(k):
    answer += diff[i]

print(answer)
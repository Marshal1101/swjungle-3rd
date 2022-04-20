# arr, brr = [3,7,2,4], [4,5,5,2]
# arr, brr = [6,2,2,6], [4,4,4,4]
answer = 0
changedValue = 0
for i in range(len(arr)):
    tmp = arr[i]-brr[i]+changedValue
    if tmp == 0:
        continue
    answer += 1
    changedValue = tmp


print(answer)
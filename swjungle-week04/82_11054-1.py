## 82 11054 가장 긴 바이토닉 부분 수열
# 참조(백준 빠른 풀이, https://www.acmicpc.net/source/16306760)

def BinarySearch(dp, value):
    left = 0
    right = len(dp)-1
    while(left<=right):
        mid = (left+right)//2            
        if dp[mid]<value:
            left=mid+1
        else:
            right=mid-1
    return left

n=int(input())
seq = [*map(int,input().split())]

dp=[seq[0]]
dp_length=[1]*n
reverse_dp_length=[1]*n

for i in range(1, n):
    if dp[-1] < seq[i]:
        dp+=[seq[i]]
        dp_length[i]=len(dp)
    else:
        idx=BinarySearch(dp, seq[i])
        dp[idx]=seq[i]
        dp_length[i]=idx+1

seq.reverse()
dp=[seq[0]]
for i in range(1, n):
    if dp[-1] < seq[i]:
        dp+=[seq[i]]
        reverse_dp_length[i]=len(dp)
    else:
        idx=BinarySearch(dp, seq[i])
        dp[idx]=seq[i]
        reverse_dp_length[i]=idx+1

print(max([dp_length[i]+reverse_dp_length[n-i-1]-1 for i in range(n)]))
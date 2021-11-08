## 작성자: 김재현

'''
problem analysis
1. 문자열을 받고 각 문자를 R번 반복 
2. r번 반복하는 함수
3. 문자열 순서대로 루프에
'''

import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(sys.stdin.readline().split()))

class Solution():
    def repeat_char(self, str, num):
        ret = []
        for char in str:
            for i in range(num):
                ret.append(char)
        return ret
    def str_extend(self, data):
        str_list = []
        for set in data:
            str_list.append(self.repeat_char(set[1], int(set[0])))
        #print(str_list)
        return str_list
if __name__ == "__main__":
    sol = Solution()
    str_list = sol.str_extend(data)
    for string in str_list:
        concat_str = "".join(string)
        print(concat_str)
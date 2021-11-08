# 작성자 김재현

import sys
data = list(map(int,sys.stdin.readline().split()))
#data = list(int(sys.stdin.readline().strip().split()))
#아 split을 하고 list로 만들어야하네 

class Solution:
    def babo_sangsoo(self, num_list):
        rev_num1 = ''.join(reversed(str(num_list[0])))
        rev_num2 = ''.join(reversed(str(num_list[1])))
        rev_num1 = int(rev_num1)
        rev_num2 = int(rev_num2)
        ret = []
        ret.append(rev_num1)
        ret.append(rev_num2)
        return max(ret)

if __name__ == "__main__":
    sol = Solution()
    print(sol.babo_sangsoo(data))

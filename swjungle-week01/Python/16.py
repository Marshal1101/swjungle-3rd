## 작성자: 김재현



## 아스키코드로 변환하는 클래스
import sys
input = sys.stdin.readline().strip()

class Solution:
    def ascii_code(self, input):
        if type(input) == int:
            return chr(input)    ## 아스키코드는 문자표준임
        else :
            return ord(input)

if __name__ == "__main__":
    sol = Solution()
    #for input in data:
    print(sol.ascii_code(input))
## 작성자 김재현

import sys
data = [int(sys.stdin.readline().strip()) for i in range(3)]
                                #세로줄로 받을 때?

class Solution:
    def get_digit_count(self, data):
        ret = data[0] * data[1] * data[2]
        count = [0 for i in range(10)]
        # count가 [0, 0, 0, 0, ....10개인 리스트] 바인딩
        ret = str(ret)
        for i in ret:
            count[int(i)] += 1
        return count
        #ret 은 잘 받았고 for문 돌리면서 count

if __name__ == "__main__":
    sol = Solution()
    num_count = sol.get_digit_count(data)
    for i in num_count:
        print(i)



# 그렇다면 인스턴스를 통해 func2를 호출하는 것과 클래스 이름을 통해 func2를 호출하는 것은
# 어떤 차이가 있을까요? 결론부터 말씀드리면 둘 사이에는 아무런 차이가 없습니다.
# 다만 ‘인스턴스.메서드()’냐 ‘클래스.메서드(인스턴스)’냐라는 차이가 있을 뿐입니다.
# 보통은 ‘인스턴스.메서드()’와 같은 방식을 주로 사용합니다.



# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 150
# 266
# 427
# 예제 출력 1 
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0
## 작성자 김재현

import sys
data=[]
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

class YourPosition:
    def get_average(self, list):
        # 파이썬 클래스에서 self의 의미를 정확히 이해하는 것이
        # 중요하지만 아직 제대로 설명하기는 조금 이른 감이 있습니다.
        # 일단 클래스 내부에 정의된 함수인 메서드의
        # 첫 번째 인자는 반드시 self여야 한다고 외우길 바랍니다.
        avg = 0
        num_list = list[1:]
        for i in num_list:
            avg += i
        return avg/list[0]

    def get_percent(self, data):
        ret = []
        for list in data:
            cnt = 0
            average = self.get_average(list)
            num_list = list[1:]
            for grade in num_list:
                if grade > average:
                    cnt += 1
            ret.append(cnt/list[0])
        return ret

if __name__ == "__main__":
    sol = YourPosition() # 클래스 대한 인스턴스 sol 생성
    per_list = sol.get_percent(data) # sol에 data 받은 메서드 get_pwercent(data)
    for i in per_list:
        print("{:.3f}%".format(100 * i))
        # "{:.3f}" 소수점3자리 실수, {}안에 들어가는 건 .format(100*i)

# 그렇다면 인스턴스를 통해 func2를 호출하는 것과 클래스 이름을 통해 func2를 호출하는 것은
# 어떤 차이가 있을까요? 결론부터 말씀드리면 둘 사이에는 아무런 차이가 없습니다.
# 다만 ‘인스턴스.메서드()’냐 ‘클래스.메서드(인스턴스)’냐라는 차이가 있을 뿐입니다.
# 보통은 ‘인스턴스.메서드()’와 같은 방식을 주로 사용합니다.







# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 예제 입력 1 
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
# 예제 출력 1 
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%
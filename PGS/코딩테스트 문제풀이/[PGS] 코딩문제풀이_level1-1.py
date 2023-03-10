### 코딩테스트 연습 > 연습문제 >
 
# 코딩테스트 level 1 

# 삼총사 (+1)

# 문제 설명 : 한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 
# 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 
# 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 
# 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 
# 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 
# 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.
# 한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 
# 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

# 제한사항 : 3 ≤ number의 길이 ≤ 13, -1,000 ≤ number의 각 원소 ≤ 1,000
# 서로 다른 학생의 정수 번호가 같을 수 있습니다.

from itertools import combinations

def solution(number):
    a = list(combinations(number, 3))
    answer = [ i for i in a if sum(i) == 0 ]
    return len(answer)




# 콜라 문제 (+7)
# 문제 설명 : 오래전 유행했던 콜라 문제가 있습니다. 콜라 문제의 지문은 다음과 같습니다.

# 정답은 아무에게도 말하지 마세요.
# 콜라 빈 병 2개를 가져다주면 콜라 1병을 주는 마트가 있다. 빈 병 20개를 가져다주면 몇 병을 받을 수 있는가?
# 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.

# 문제를 풀던 상빈이는 콜라 문제의 완벽한 해답을 찾았습니다. 상빈이가 푼 방법은 아래 그림과 같습니다. 
# 우선 콜라 빈 병 20병을 가져가서 10병을 받습니다. 받은 10병을 모두 마신 뒤, 가져가서 5병을 받습니다. 
# 5병 중 4병을 모두 마신 뒤 가져가서 2병을 받고, 또 2병을 모두 마신 뒤 가져가서 1병을 받습니다. 
# 받은 1병과 5병을 받았을 때 남은 1병을 모두 마신 뒤 가져가면 1병을 또 받을 수 있습니다. 
# 이 경우 상빈이는 총 10 + 5 + 2 + 1 + 1 = 19병의 콜라를 받을 수 있습니다.

# 문제를 열심히 풀던 상빈이는 일반화된 콜라 문제를 생각했습니다. 
# 이 문제는 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산하는 문제입니다. 
# 기존 콜라 문제와 마찬가지로, 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없습니다. 
# 상빈이는 열심히 고심했지만, 일반화된 콜라 문제의 답을 찾을 수 없었습니다. 
# 상빈이를 도와, 일반화된 콜라 문제를 해결하는 프로그램을 만들어 주세요.

# 콜라를 받기 위해 마트에 주어야 하는 병 수 a, 
# 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 
# 상빈이가 가지고 있는 빈 병의 개수 n이 매개변수로 주어집니다. 
# 상빈이가 받을 수 있는 콜라의 병 수를 return 하도록 solution 함수를 작성해주세요.

# my ver.
def solution(a, b, n):
    quotient = 0
    take_coke = 0
    while n >= a:
        quotient = n // a
        n = n - (quotient * a) + (quotient * b)
        take_coke += quotient * b
    return take_coke

# short ver.
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b
# 한꺼번에 계산하지 않고 a개만 팔고 b개를 받는 과정은 결국 a-b 개씩 병을 소비하는 것으로 생각, 
# 첫번째 진행할 때는 a개만 소비되기 때문에, b만큼 못받음(-b), 
# 그 조건을 먼저 계산 n-b 반복횟수는 n-b // (a-b) 여기에 받는 병수 b 곱한 것 
### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 8 배열, 구현, 수학
# 배열 자르기 (+1)
# 문제 설명 : 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]


# 외계 행성의 나이 (+1)
# 문제 설명 : 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
#  입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
#  a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다.
#  나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# ver1. 런타임 에러 발생
def solution(age):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in str(age):
        answer += alphabet[int(i)]
    return answer

# ver2. 아스키 코드
def solution(age):
    answer =''
    return answer.join([chr(int(i)+97) for i in str(age)])


# 진료 순서 정하기 (+1)
# 문제 설명 : 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(emergency: list) -> list:
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    # 인덱스를 0이 아니라, 1로 시작하고 싶을 때, enumerate() 함수를 호출 시 start 인자에 시작하고 싶은 숫자를 넘기면 됨.
    
    return [dict[x] for x in emergency]

# 순서쌍의 개수 (+3)
# 문제 설명 : 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return len(answer)
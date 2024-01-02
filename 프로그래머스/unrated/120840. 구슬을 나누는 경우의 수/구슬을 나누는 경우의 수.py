# 조합 라이브러리가 있지않을까?
from math import comb

def solution(balls, share):
    return comb(balls, share)

# 아니면 팩토리얼 함수 만들기
def solution(balls, share):
    numer = factorial(balls)
    denom = factorial(balls - share) * factorial(share)
    return numer/denom

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)

# 의사코드
    # 조합 라이브러리가 있지않을까?
    
    # 아니면 팩토리얼 함수 만들기
    # n! = n(n-1)(n-2)...1

# 근데 팩토리얼 라이브러리도 있었음ㅋㅋ
from math import factorial as f
def solution(balls, share):
    return f(balls)/(f(share)*f(balls-share))

# 계산으로 풀이(팩토리얼을 한번에 계산)
def solution(balls, share):
    a, b = 1, 1
    for i in range(1,share+1):
        a *= balls
        balls -= 1
        b *= i
    return int(a / b)

# 다른방식의 팩토리얼
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

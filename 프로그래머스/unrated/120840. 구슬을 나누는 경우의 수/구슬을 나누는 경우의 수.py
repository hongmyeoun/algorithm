from math import comb

# def solution(balls, share):
#     return comb(balls, share)

# 의사코드
    # 조합 라이브러리가 있지않을까?
    
    # 아니면 팩토리얼 함수 만들기
    # n! = n(n-1)(n-2)...1
    
def solution(balls, share):
    numer = factorial(balls)
    denom = factorial(balls - share) * factorial(share)
    return numer/denom

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)
import math

def solution(a, b):

    gcd = math.gcd(a,b)
    denom = b//gcd
    
    result = 0
    
    if a == b:
        return 1
    
    if not a % b:
        return 1
    
    for i in prime_factors(denom):
        if i == 2 or i == 5:
            result = 1
        else:
            return 2
    return result

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return list(set(factors))

# 의사코드
    # 일단 분자 분모를 기약분수로 만듦
    # 최대공약수로 약분
    # 이후 분모의 소인수를 찾음
    # 소인수가 2 또는 5가 아니면 2를 return

test case를 통과 못해서 몇개 추가
1. a == b일때
2. a가 b로 나누어 떨어질때
이때도 유한소수이다.

소인수에 2나 5가 아닌 다른수가 나왔을때 바로 break를 통해 결과를 return해야 테스트가 통과 됐다.

# 다른 풀이
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

기약분수를 2로 나누고 5로나눠 몫이 1이 아니면 바로 무한소수인 방법

# 비슷한 방법
from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2

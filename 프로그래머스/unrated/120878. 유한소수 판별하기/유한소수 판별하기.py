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
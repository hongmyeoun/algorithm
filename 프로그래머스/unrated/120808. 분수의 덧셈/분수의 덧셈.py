def solution(numer1, denom1, numer2, denom2):

    denom_lcm = LCM(denom1, denom2)
    numer = denom_lcm//denom1*numer1 + denom_lcm//denom2*numer2
    gcd = GCD(divisor(numer), divisor(denom_lcm))
    
    answer = [numer//gcd, denom_lcm//gcd]
    
    return answer

def LCM(denom1, denom2):
    for i in range(1, denom1 * denom2 + 1):
        if not i % denom1 and not i % denom2:
            return i
        
def divisor(n): 
    return [i for i in range(1, n+1) if not n % i]

def GCD(divisor_list1, divisor_list2):
    return max(list(set(divisor_list1) & set(divisor_list2)))

# 의사코드
    # 통분
        # 분모
            # 분모의 최소공배수를 찾음
            # 최소공배수(LCM)
                # 1부터 분모 둘을 곱한수까지 반복
                # 그 수를 분모로 나눴을때 나머지가 0인 수(둘다 0일때)
        # 분자
            # 최소공배수를 분모로 나눈 값(몫)을 곱해줌
    
    # 덧셈
        # 이후 둘이 더함
    
    # 약분
        # 분모와 분자를 최대공약수로 나눔
            # 최대공약수(GCD)
                # 두 수의 공약수 중 가장 큰 값
                # 공약수
                    # 두 수의 약수중 공통된 값
                    # 분자의 약수를 구함, 분모의 약수를 구함(이전에 푼 약수식 기억해내자)
                    # 둘의 공통부분을 가져옴
                # max(공약수)

함수들이 간단해서 람다식으로 만들어도 됐지만 LCM을 람다식으로 못 만들겠어서 def로 통일
numer을 계산할때 lcm을 분모로 나눈수를 분자에 곱하는 부분이 LCM을 denom으로 받았었는데 뭔가 변수이름이 이상해서 고침

지금 생각하니 방법이 두가지가 있는데
1. 최소공배수로 통분을 하고 더하고 최대공약수로 약분하는 방법(내방법)
2. 그냥 통분해 더한후 최대공약수로 나누는 방법
2번방법으로 풀이를 하면 식은 간단해질 것 같음, 실제로 손으로 문제풀때 그냥 곱하면 큰수에서 맨날 계산실수나서 안해서 저리 안품...

# 바꾼 풀이(GCD만)
def solution(numer1, denom1, numer2, denom2):

    numer = denom1*numer1 + denom2*numer2
    denom = denom1*denom2
    gcd = GCD(divisor(numer), divisor(denom))
    
    answer = [numer//gcd, denom//gcd]
    
    return answer

def divisor(n): 
    return [i for i in range(1, n+1) if not n % i]

def GCD(divisor_list1, divisor_list2):
    return max(list(set(divisor_list1) & set(divisor_list2)))

# 최소공배수로 곱한것이 아니라 그냥 곱하고 최대공약수로 나누는 케이스(다른사람)
def solution(numer1, denom1, numer2, denom2):
    num_sum = numer1 * denom2 + numer2 * denom1
    dem_sum = denom1 * denom2
    for i in range(2,dem_sum):
        while dem_sum%i==0 and num_sum%i==0:
            dem_sum //= i
            num_sum //= i

    return [num_sum, dem_sum]

# math 라이브러리 활용(작성자가 다 반대로 써둠(파라미터))
import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom)
    return [numer//gcd, denom//gcd]

# Fraction 라이브러리 사용
from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]

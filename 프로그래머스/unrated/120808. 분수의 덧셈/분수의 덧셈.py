def solution(numer1, denom1, numer2, denom2):
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
    denom = LCM(denom1, denom2)
    numer = denom//denom1*numer1 + denom//denom2*numer2
    gcd = GCD(divisor(numer), divisor(denom))
    
    answer = [numer//gcd, denom//gcd]
    
    return answer

def LCM(denom1, denom2):
    for i in range(1, denom1 * denom2 + 1):
        if not i % denom1 and not i % denom2:
            return i
        
def divisor(n):
    return [i for i in range(1, n+1) if not n % i]
# divisor = lambda n: [i for i in range(1, n+1) if not n % i]
# 통일성?을 위해 def로 만듦

def GCD(divisor_list1, divisor_list2):
    return max(list(set(divisor_list1) & set(divisor_list2)))
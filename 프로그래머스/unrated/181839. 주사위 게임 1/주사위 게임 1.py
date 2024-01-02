def solution(a, b):
    if a%2 == 1 and b%2 == 1:
        return a**2 + b**2
    elif (a%2 == 0 and b%2 == 1) or (a%2 == 1 and b%2 == 0):
        return 2 * (a + b)
    return abs(a-b)

# if문 조건 간소화
def solution(a, b):
    if a%2 and b%2: 
        return a*a+b*b
    elif a%2 or b%2: # 둘 중 하나만 참이라도 true니깐 둘쭝 하나만 홀수여도 된다는 뜻
        return 2*(a+b)
    return abs(a-b)

0은 false
1은 true

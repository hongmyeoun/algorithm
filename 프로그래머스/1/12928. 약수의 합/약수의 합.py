def solution(n):
    return sum(i for i in range(1,n+1) if n%i==0)

# 0.5제곱만 판단
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

12 -> 1, 2, 3, 4, 6, 12
약수는 자신의 반을 넘어가는 수보다 클수 없음
반을 넘는 수는 자기 자신만 있기 때문 num을 앞에 더해줌

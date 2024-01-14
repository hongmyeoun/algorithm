def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        if divisor_counter(i) <= limit:
            answer += divisor_counter(i)
        else:
            answer += power
    return answer

def divisor_counter(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return len(divisors)

# number -> 기사단의 번호(1번부터 number번 까지)
# limit -> 약수의 개수를 확인하는 제한조건, 넘으면 power만큼 계산
# power -> 협약 조건, limit가 넘은 기사단의 무기를 power로 강제화

# 1~number까지의 list를 만들어 약수의 개수를 판별
# 약수의 개수가 limit을 넘어가지 않는다면 answer 에 더함
# 넘어간다면 power를 더함
# answer return
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor_len(i)%2 == 0:
            answer += i
        else:
            answer += -i
            
    return answer

def divisor_len(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if not n%i:
            result.add(i)
            result.add(n/i)
    return len(result)

# 간단히 약수구하기
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


약수의 개수가 홀수인지 짝수인지를 판단하는데는 다음과 같은 규칙이 적용됩니다.

약수의 쌍: 어떤 수 n의 약수를 구한다고 생각해봅시다. 예를 들어, n의 약수가 a라면 반드시 그에 대응하는 약수 b도 존재합니다. 즉, a * b = n이 성립합니다.

약수의 중복 제거: 하지만 이렇게 약수를 나열하면 중복된 쌍이 발생할 수 있습니다. 예를 들어, n이 9일 경우 약수는 (1, 9), (3, 3)으로 중복된 약수가 있습니다.

완전 제곱수의 특징: 그러나 완전 제곱수인 경우에는 중복된 약수가 발생하지 않습니다. 완전 제곱수는 어떤 수를 제곱한 것이기 때문에 약수들이 중복되지 않고 정확히 나누어떨어집니다.

따라서, 어떤 수 n의 약수의 개수가 홀수인지 짝수인지를 판단하려면 완전 제곱수인지 아닌지를 확인하면 됩니다. 완전 제곱수인 경우 약수의 개수는 홀수이고, 완전 제곱수가 아닌 경우 약수의 개수는 짝수입니다.

if int(i**0.5) == i**0.5이 부분은 i가 완전 제곱수인지를 판단합니다. 만약 i가 완전 제곱수라면, i의 약수의 개수는 홀수이고, 조건은 참이 됩니다. 반면에 i가 완전 제곱수가 아니라면, i의 약수의 개수는 짝수이고, 조건은 거짓이 됩니다.

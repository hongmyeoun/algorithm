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
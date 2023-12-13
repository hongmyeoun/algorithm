def solution(num, n):
    answer = 1 if num % n == 0 else 0
    return answer

# 다른사람 풀이
def solution(num, n):
    return int(not(num % n))

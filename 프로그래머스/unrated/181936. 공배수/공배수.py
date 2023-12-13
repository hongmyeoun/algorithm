def solution(number, n, m):
    answer = 1 if number % n == 0 and number % m == 0 else 0
    return answer

# 다른사람 풀이
def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))

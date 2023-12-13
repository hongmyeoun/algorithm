def solution(n):
    answer = sum([i for i in range(1, n+1, 2)]) if n % 2 == 1 else sum([i*i for i in range(2, n+1, 2)])
    return answer

# 다른사람의 풀이
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

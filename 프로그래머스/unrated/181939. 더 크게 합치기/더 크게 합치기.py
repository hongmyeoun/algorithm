def solution(a, b):
    a, b = str(a), str(b)
    answer = int(a + b) if int(a + b) > int(b + a) else int(b + a)
    return answer

# 다른사람 풀이 1

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# 다른사람 풀이 2

def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a+b, b+a))

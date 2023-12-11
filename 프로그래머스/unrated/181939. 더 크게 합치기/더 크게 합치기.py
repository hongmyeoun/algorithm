def solution(a, b):
    a, b = str(a), str(b)
    answer = int(a + b) if int(a + b) > int(b + a) else int(b + a)
    return answer
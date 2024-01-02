def solution(n):
    result = 0
    for i in list(str(n)):
        result += int(i)
    return result
def solution(n, k):
    answer = []
    result = 0
    i = 1
    while True:
        result = i * k
        if result <= n:
            answer.append(result)
            i += 1
        else:
            break
        
    return answer
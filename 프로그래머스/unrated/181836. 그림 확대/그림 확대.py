def solution(picture, k):
    answer = []
    result = ''
    for p in picture:
        for c in p:
            result = result + c*k
        for _ in range(k):
            answer.append(result)
        result = ''
    return answer
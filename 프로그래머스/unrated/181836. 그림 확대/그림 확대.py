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

# replace로 하기
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer

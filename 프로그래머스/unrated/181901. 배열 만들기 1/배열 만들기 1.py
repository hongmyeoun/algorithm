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

# 위 코드 더 간결화
def solution(n, k):
    answer = []
    i = 1
    while (i * k) <= n: answer.append(i * k); i += 1
    return answer

# 리스트 컨프리헨션 답안
def solution(n, k):
    return [i for i in range(k,n+1,k)]

k부터 시작해 더하는 형식

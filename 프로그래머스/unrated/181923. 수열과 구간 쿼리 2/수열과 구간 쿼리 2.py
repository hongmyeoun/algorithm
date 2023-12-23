def solution(arr, queries):
    # s부터 e까지 k보다 크면서 가장작은 값 찾기
    answer = []
    for query in queries:
        s, e, k = query
        result = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        answer.append(min(result) if result else -1)

    return answer

# 처음 코드
def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        result = []
        for i in range(s, e + 1):
            if arr[i] > k:
                result = arr[i]
        if result:
            answer.append(min(result))
        else:
            answer.append(-1)
    return answer
    
# 첫 코드와 비슷한 코드
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

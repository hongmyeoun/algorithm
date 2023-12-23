def solution(arr, queries):
    # s부터 e까지 k보다 크면서 가장작은 값 찾기
    answer = []
    for query in queries:
        s, e, k = query
        # 처음 코드
        # result = []
        # for i in range(s, e + 1):
        #     if arr[i] > k:
        #         result = arr[i]
        # if result:
        #     answer.append(min(result))
        # else:
        #     answer.append(-1)
        result = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        answer.append(min(result) if result else -1)

    return answer
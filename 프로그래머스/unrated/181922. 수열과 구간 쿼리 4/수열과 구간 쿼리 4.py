def solution(arr, queries):
    # 처음코드
    for query in queries:
        s, e, k = query
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] = arr[i] + 1
    return arr
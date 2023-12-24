def solution(arr, queries):
    # 처음코드
    for query in queries:
        s, e, k = query
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] = arr[i] + 1
    return arr

# 다른 코드
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        for i in range(s, e+1):
            # not은 나머지가 0이면 True 아니면 false
            if not i % k:
                arr[i] += 1
    return arr

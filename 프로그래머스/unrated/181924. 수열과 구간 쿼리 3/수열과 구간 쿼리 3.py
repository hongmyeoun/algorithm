def solution(arr, queries):
    for query in queries:
        arr[query[0]], arr[query[1]] = arr[query[1]], arr[query[0]]
    return arr

# 받을때부터 두개로 받기
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr

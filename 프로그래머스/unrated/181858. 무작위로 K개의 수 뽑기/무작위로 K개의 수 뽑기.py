def solution(arr, k):

    arr_set = dict.fromkeys([str(i) for i in arr])
    arr_set = [int(i) for i in list(arr_set)]
    if len(arr_set[:k]) < k:
        return arr_set[:k] + [-1]*(k-len(arr_set[:k]))
    return arr_set[:k]

# not in으로 유니크 찾기
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))

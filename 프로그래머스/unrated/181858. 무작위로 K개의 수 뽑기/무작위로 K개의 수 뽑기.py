def solution(arr, k):

    arr_set = dict.fromkeys([str(i) for i in arr])
    arr_set = [int(i) for i in list(arr_set)]
    if len(arr_set[:k]) < k:
        return arr_set[:k] + [-1]*(k-len(arr_set[:k]))
    return arr_set[:k]
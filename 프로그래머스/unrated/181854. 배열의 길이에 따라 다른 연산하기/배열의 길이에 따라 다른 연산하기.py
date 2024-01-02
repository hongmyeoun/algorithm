def solution(arr, n):
    for idx, i in enumerate(arr):
        if len(arr)%2:
            if idx%2 == 0:
                arr[idx] = i+n
        else:
            if idx%2:
                arr[idx] = i+n
    return arr
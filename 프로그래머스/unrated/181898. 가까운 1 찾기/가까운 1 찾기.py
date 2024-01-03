def solution(arr, idx):
    for index, i in enumerate(arr):
        if idx <= index and i:
            return index
    return -1
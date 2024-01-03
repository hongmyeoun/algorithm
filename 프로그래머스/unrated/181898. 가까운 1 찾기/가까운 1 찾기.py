def solution(arr, idx):
    for index, i in enumerate(arr):
        if idx <= index and i:
            return index
    return -1

# range로 해결
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

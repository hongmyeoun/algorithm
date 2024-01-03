def solution(arr, delete_list):
    result = []
    for i in range(len(arr)):
        if not (arr[i] in delete_list):
            result.append(arr[i])
    return result
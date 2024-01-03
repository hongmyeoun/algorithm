def solution(arr, delete_list):
    result = []
    for i in range(len(arr)):
        if not (arr[i] in delete_list):
            result.append(arr[i])
    return result

# 간단하게 
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]

# remove 활용
def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == len(arr)-1:
            if arr[i] == arr[-1]:
                answer.append(arr[i])
            else:
                answer.append(arr[i])
                answer.append(arr[-1])
        elif arr[i]==arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    return answer
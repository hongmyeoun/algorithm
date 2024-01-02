def solution(arr):
    for idx, i in enumerate(arr):
        if i >= 50 and i%2 == 0:
            arr[idx] = i/2
        elif i < 50 and i%2 == 1:
            arr[idx] = i*2
                
    return arr
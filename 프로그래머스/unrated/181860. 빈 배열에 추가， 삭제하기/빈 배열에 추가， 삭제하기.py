def solution(arr, flag):
    X = []
    for i, j in zip(arr, flag):
        if j:
            for _ in range(i*2):
                X.append(i)
        else:
            for _ in range(i):
                X.pop()    
    return X
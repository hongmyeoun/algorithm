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

# enumerate()로 풀이
def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]] * (arr[i]*2)
        else:
            for _ in range(arr[i]):
                X.pop()
    return X

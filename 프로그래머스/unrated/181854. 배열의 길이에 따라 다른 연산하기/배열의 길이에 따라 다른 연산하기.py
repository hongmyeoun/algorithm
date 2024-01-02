def solution(arr, n):
    for idx, i in enumerate(arr):
        if len(arr)%2:
            if idx%2 == 0:
                arr[idx] = i+n
        else:
            if idx%2:
                arr[idx] = i+n
    return arr

# 직관적인 코드(for문을 조건에 따라서 돌리는데 이게 더 효율적인가?)
def solution(arr, n):
    if len(arr) % 2:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n

    return arr

효율차이는 없다고 한다. 다만 위 코드에 불필요한 enumerate()함수를 없에면 더 직관적일 수 있다고 한다.

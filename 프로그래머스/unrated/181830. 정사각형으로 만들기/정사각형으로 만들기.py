def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    # 행의 수가 더 많으면 열을 행과 맞추기
    if num_rows > num_cols:
        for row in arr:
            row += [0] * (num_rows - num_cols)
    elif num_cols > num_rows:
        for _ in range(num_cols - num_rows):
            arr.append([0]*num_cols)
    return arr
def solution(board):
    coordinate = set() # [0,1,1,0,0] 이런식이면 1과 1이 겹치므로 중복이 생김 그건 제외
    n = len(board)
    for i, row in enumerate(board): #[0,0,0,0,0]
        for j, col in enumerate(row): # 0
            if col == 1:
                for x in (-1, 0, 1): # [0,1,1,1,0]
                    for y in (-1, 0, 1): # [0,1,1,1,0] * 3
                        if -1 < i + x < n and -1 < j + y < n: # 범위지정 0<= <=길이-1
                            coordinate.add((i + x, j + y)) # 1인 좌표 등록(중복 제외)
    return n * n - len(coordinate)

# update로 풀이
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

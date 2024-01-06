def solution(n):
    answer = [[0]*n for _ in range(n)] # 0으로 채워진 배열 생성
    # [우 하 상 좌] 순으로 벽에 부딪혔을때 방향설정
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    x, y = 0, 0 # 초기 좌표
    direction = 0 # 방향설정(dx, dy로) 0,1,2,3
    
    for i in range(1, (n*n)+1):
        answer[y][x] = i # 빈배열에 i넣기
        
        # 이동할 다음 좌표
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 이동할 다음 좌표가 벽에 부딛히거나 숫자가 들어왔을때 다음 좌표 구하기
        if nx >= n or nx < 0 or ny >= n or ny  < 0 or answer[ny][nx] != 0:
            
            direction = (direction + 1) % 4 #4방향
            
            # 방향 정한후 이동좌표 구하기
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x, y = nx, ny # 좌표이동
    return answer
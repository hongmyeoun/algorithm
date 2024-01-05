def solution(keyinput, board):
    answer = [0,0]
    end_line_hl = -(board[0] - 1) / 2
    end_line_hr = (board[0] - 1) / 2
    end_line_vd = -(board[1] - 1) / 2
    end_line_vu = (board[1] - 1) / 2
    
    for direction in keyinput:
        if direction == 'left':
            if answer[0] != end_line_hl:
                answer[0] -= 1
        elif direction == 'right':
            if answer[0] != end_line_hr:
                answer[0] += 1
        elif direction == 'down':
            if answer[1] != end_line_vd:
                answer[1] -= 1
        elif direction == 'up':
            if answer[1] != end_line_vu:
                answer[1] += 1
    return answer

# max, min으로 최적값으로 가기
def solution(keyinput, board):
    curr = [0, 0]
    for k in keyinput:
        if k == 'left':
            curr[0] = max(curr[0] - 1, -(board[0] // 2))
        elif k == 'right':
            curr[0] = min(curr[0] + 1, board[0] // 2)
        elif k == 'down':
            curr[1] = max(curr[1] - 1, -(board[1] // 2))
        else:
            curr[1] = min(curr[1] + 1, board[1] // 2)

    return curr

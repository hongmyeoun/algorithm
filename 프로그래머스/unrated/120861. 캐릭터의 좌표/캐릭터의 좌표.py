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
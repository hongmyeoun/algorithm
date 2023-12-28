def solution(my_string, m, c):
    matrix = [list(my_string[i:i + m]) for i in range(0, len(my_string), m)]
    return ''.join([matrix[i][c-1] for i in range(len(matrix))])
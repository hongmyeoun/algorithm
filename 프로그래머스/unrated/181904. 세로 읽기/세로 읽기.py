def solution(my_string, m, c):
    matrix = [list(my_string[i:i + m]) for i in range(0, len(my_string), m)] # range(start, end, step)
    return ''.join([matrix[i][c-1] for i in range(len(matrix))])

# 충격과 공포의 슬라이싱
solution = lambda my_string, m, c: my_string[c-1::m] 
# c-1 : 슬라이싱 시작 인덱스
# ::m : 슬라이싱 간격
# -> 이 풀이가 문제와 적합한지 의문이 듦, 2차원 리스트를 만들고 각 열에 대한 정보를 갖고오는 취지인것 같은 문제인데, 이 풀이는 str슬라이싱
# 하지만 매우 합리적임

# 이것도 비슷한 방법
def solution(my_string, m, c):
    return ''.join(my_string[i] for i in range(c - 1, len(my_string), m))

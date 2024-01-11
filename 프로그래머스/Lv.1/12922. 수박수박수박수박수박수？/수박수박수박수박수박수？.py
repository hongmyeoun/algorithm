def solution(n):
    answer = ''
    for i in range(n):
        if i%2:
            answer += '박'
        else:
            answer += '수'
    return answer

# 슬라이싱
def water_melon(n):
    str = "수박"*n
    return str[:n]

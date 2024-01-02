def solution(n):
    x = 1
    while True:
        if n*x % 6 == 0:
            return n*x//6
        else:
            x += 1


# while 조건을 추가
def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer

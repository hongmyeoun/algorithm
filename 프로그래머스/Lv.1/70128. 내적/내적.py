def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i*j
    return answer

# +=를 굳이 안하고 리스트컴프리헨션에 넣자
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

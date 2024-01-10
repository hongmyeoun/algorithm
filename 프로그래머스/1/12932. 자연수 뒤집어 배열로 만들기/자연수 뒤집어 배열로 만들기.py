def solution(n):
    answer = []
    for i in str(n):
        answer.insert(0, int(i))
    return answer

# 처음 구상한 생각
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

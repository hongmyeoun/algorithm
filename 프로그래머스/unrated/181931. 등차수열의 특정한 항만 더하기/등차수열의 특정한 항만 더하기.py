def solution(a, d, included):
    sum_true = 0
    for idx, i in enumerate(included):
        if i:
            sum_true += a + d * idx
    return sum_true

# 다른사람 코드
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

# 한줄코드
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)

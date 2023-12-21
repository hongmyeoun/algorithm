def solution(a, d, included):
    sum_true = 0
    for idx, i in enumerate(included):
        if i:
            sum_true += a + d * idx
    return sum_true
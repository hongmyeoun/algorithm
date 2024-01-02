def solution(num_list):
    answer = [1 if i % 2 == 0 else 2 for i in num_list]
    return [answer.count(1), answer.count(2)]
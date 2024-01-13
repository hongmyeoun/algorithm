def solution(name, yearning, photo):
    answer = []
    for i in photo:
        point = 0
        for n, y in zip(name, yearning):
            for man in i:
                if man == n:
                    point += y
        answer.append(point)
    return answer
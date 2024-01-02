def solution(num, total):
    answer = []
    end = int((((total * 2) / num) + num - 1) / 2)
    while num > 0:
        answer.append(end)
        end -= 1
        num -= 1
    answer.sort()
    return answer

# m == (((total * 2) / n) + n - 1) / 2


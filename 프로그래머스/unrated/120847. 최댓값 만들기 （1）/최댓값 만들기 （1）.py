def solution(numbers):
    numbers.sort()
    return numbers[len(numbers)-1] * numbers[len(numbers)-2]

# 인덱싱 연습좀...
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

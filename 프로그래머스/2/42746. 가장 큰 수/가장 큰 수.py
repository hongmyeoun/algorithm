def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    max_len = len(str(max(numbers)))
    numbers.sort(key=lambda x: str(x) * (max_len // len(str(x))) + str(x), reverse=True)
    return ''.join(map(str, numbers))

# 숫자 뒤에 그 숫자를 반복해 비교

# def solution(numbers):
#     max_len = len(str(max(numbers)))
#     numbers.sort(key=lambda x: str(x).ljust(max_len, str(x)[-1]), reverse=True)
#     return ''.join(map(str, numbers))

# 자리수가 다른 값을 비교할때 자리수를 맞춰서 비교
# 더 적은 자리수는 일의 자리 숫자로 채워서 큰자리수와 자리수를 맞춤
# ex) 3과 30을 비교하면
# 33과 30을 비교하는 꼴

def solution(x):
    digit = list(str(x))
    digit = [int(i) for i in digit]
    digit_sum = 0
    for i in digit:
        digit_sum += i
    return True if x%digit_sum == 0 else False
def solution(x):
    digit = list(str(x))
    digit = [int(i) for i in digit]
    digit_sum = 0
    for i in digit:
        digit_sum += i
    return True if x%digit_sum == 0 else False


# 똑같은 식을 정리하기
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

def solution(n):
    if n > 7:
        if n % 7 == 0:
            return n // 7
        else:
            return n // 7 + 1
    else:
        return 1

# 의사코드
    # 피자 한판 개수 = 7 * x
    # n 7 피자 7, 사람 7 -> 1
    # n 1 피자 7, 사람 1 -> 1
    # n 15 사람 15, 피자 21 -> 3

# Wow
def solution(n):
    return (n - 1) // 7 + 1

def solution(n):
    for i in range(n):
        if n == i**2:
            return 1
    return 2

# is_interger()
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

def solution(n):
    x = pow(n, 0.5)
    if x.is_integer():
        return pow(x+1, 2)
    return -1
def solution(n):
    one = bin(n).count("1")
    n += 1
    while True:
        if one == bin(n).count("1"):
            break
        else:
            n += 1
    return n
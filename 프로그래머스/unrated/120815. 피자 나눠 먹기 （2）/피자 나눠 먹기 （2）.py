def solution(n):
    x = 1
    while True:
        if n*x % 6 == 0:
            return n*x//6
        else:
            x += 1

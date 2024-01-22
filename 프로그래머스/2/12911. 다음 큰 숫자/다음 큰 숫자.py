def solution(n):
    one = bin(n).count("1")
    n += 1
    while True:
        if one == bin(n).count("1"):
            break
        else:
            n += 1
    return n

# 순서를 바꾸면 반박문 위에 값을 안넣어도 된다
def solution(n):
    one = bin(n).count("1")
    while True:
        n += 1
        if one == bin(n).count("1"):
            break
    return n

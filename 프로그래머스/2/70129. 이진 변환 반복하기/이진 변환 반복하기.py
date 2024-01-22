def solution(s):
    answer = []
    zeros = 0
    count = 0
    while int(s)!=int("1",2):
        s, zero = x_bin(s)
        zeros += zero
        count += 1
    return count, zeros

def x_bin(x):
    zero = x.count("0")
    x = bin(x.count("1"))[2:]
    return x, zero


# 하나의 함수에서
def solution(s):
    iteration, count = 0, 0
    while s != '1':
        iteration += 1
        count += s.count('0')
        s = bin(s.count('1'))[2:]
    return [iteration, count]

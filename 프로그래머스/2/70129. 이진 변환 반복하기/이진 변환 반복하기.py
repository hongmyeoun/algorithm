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
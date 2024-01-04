from math import factorial

def solution(n):
    for i in range(2, 11):
        if factorial(i) == n:
            return i
        elif factorial(i) > n:
            return i-1
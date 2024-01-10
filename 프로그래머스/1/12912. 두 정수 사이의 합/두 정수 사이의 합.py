from functools import reduce

def solution(a, b):
    return reduce(lambda x,y: x+y, list(range(min(a, b), max(a, b)+1)))
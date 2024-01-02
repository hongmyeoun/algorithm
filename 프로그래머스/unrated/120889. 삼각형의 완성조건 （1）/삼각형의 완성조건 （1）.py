def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[-1] else 2

# 총합 - 최대 = 나머지
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

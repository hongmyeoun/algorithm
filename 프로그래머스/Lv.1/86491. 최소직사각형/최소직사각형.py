def solution(sizes):
    answer = 0
    left = []
    right = []
    for i in sizes:
        left.append(max(i))
        right.append(min(i))
        
    return max(left) * max(right)

# 14 4
# 19 6
# 16 6
# 18 7
# 11 7

# 19 7

# 10 7
# 12 3
# 15 8
# 14 7
# 15 5

# 15 8

# 60 50
# 70 30
# 60 30
# 80 40

# 80 50

# [max, min]으로 정렬한뒤, max의 max값과 min의 max값을 곱함

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

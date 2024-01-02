def solution(sides):

    sides.sort()
    other_max = sum(sides)
    in_max = sides[1]
    in_min = sides[0]
    
    return len(range(in_max+1, other_max)) + len(range(in_max-in_min+1, in_max+1))

# 의사코드
    # # 가장 긴 변의 길이는 두 변의 길이의 합보다 작아야 함
    # 1, 2
    # 1 + 2 = 3
    # 가장긴변 2 < a < 3, X
    # 2가가장 길면
    # 1 + a > 2, 2 >= a > 1, [2]
    # 3, 6
    # 3 + 6 = 9
    # 가장긴변 6 < a < 9, [7, 8]
    # 6이 가장길면
    # 3 + a > 6, 6 >= a > 3, [4, 5, 6]
    # 11, 7
    # 11 + 7 = 18
    # 가장긴변 11 < a < 18, [12,13,14,15,16,17]
    # 11이가장 길면
    # 7 + a > 11, 11 >= a > 4, [5,6,7,8,9,10,11]
    # # 나머지 한 변이 될 수 있는 정수의 개수
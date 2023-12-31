def solution(dots):
    delta = []
    for idx, a in enumerate(dots):
        for b in dots[idx+1:]:
            delta.append(abs((b[1]-a[1])/(b[0]-a[0])))
    # delta = [AB,AC,AD,BC,BD,CD]
    return 1 if delta[0] == delta[-1] or delta[1] == delta[-2] or delta[2] == delta[3] else 0

# dy/dx = 기울기
# 기울기가 같은것이 답
# 반례로 [[1, 2], [2, 1], [3, 4], [4, 5]] 일때 기댓값이 0이라는데
# 눈으로 봐도 1,2/3,4 랑 2,1/4,5랑 이은건 평행임
# 하지만 문제는 한점에서 시작되는 점을 고려하지 않음

# def solution(dots):
#     [[x1,y1],[x2,y2],[x3,y3],[x4,y4]] = dots # a, b, c, d
#     # 평행 검사 선분은 AB-CD, AC-BD, AD-BC 이렇게 세개
#     # 필요한 기울기는 AB, AC, AD, BC, BD, CD
#     delta_AB = abs((y2-y1)/(x2-x1)) # 선분 AB의 기울기
#     delta_AC = abs((y3-y1)/(x3-x1)) # 선분 AC의 기울기
#     delta_AD = abs((y4-y1)/(x4-x1)) # 선분 AD의 기울기
    
#     delta_BC = abs((y3-y2)/(x3-x2)) # 선분 BC의 기울기
#     delta_BD = abs((y4-y2)/(x4-x2)) # 선분 BD의 기울기
    
#     delta_CD = abs((y4-y3)/(x4-x3)) # 선분 CD의 기울기
    
#     return 1 if delta_AB == delta_CD or delta_AC == delta_BD or delta_AD == delta_BC else 0

# 숏코딩 햄스터
from functools import reduce
def solution(dots):
    return int(max(reduce(lambda dict, x: dict.update({x: dict.get(x, 0)+1}) or dict,[(d1[1] - d2[1])/(d1[0]-d2[0]) if d1[0]-d2[0] else "x" for d1 in dots for d2 in dots if not d1==d2], {}).values()) > 2)

reduce(람다식, 리스트)
numbers_addition = [1, 2, 3, 4, 5]
result_addition = reduce(lambda x, y: x + y, numbers_addition)
결과 : 15 # 1~5까지 더함

numbers_multiplication = [1, 2, 3, 4, 5]
result_multiplication = reduce(lambda x, y: x * y, numbers_multiplication)
결과 : 120 # 1~5까지 곱함

람다식을 리스트에 적용해 더한값을 반환

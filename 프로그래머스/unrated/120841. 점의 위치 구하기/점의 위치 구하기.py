def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    else:
        if dot[1] > 0:
            return 2
        else:
            return 3

def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

좀 더 발전시켜서 quad = [(2, 1), (3, 4)]; return quad[dot[1]<0][dot[0]>0] 로 하면, 사분면 위치랑도 맞아서 좋네요

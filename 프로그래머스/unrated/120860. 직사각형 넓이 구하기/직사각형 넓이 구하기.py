def solution(dots):
    for i in range(len(dots)):
        if dots[0][0] != dots[i][0]:
            width = abs(dots[i][0] - dots[0][0])
        if dots[0][1] != dots[i][1]:
            height = abs(dots[i][1] - dots[0][1])
    return width * height

# 의사코드
    # 입력 순서가 [아래왼쪽, 아래오른쪽, 위오른쪽, 위왼쪽]으로 고정이면
    # |아래오른쪽 x좌표 - 아래왼쪽 x좌표| * |위왼쪽 y좌표 - 아래왼쪽 y좌표|
    # abs(dots[1][0] - dots[0][0]) * abs(dots[3][1] - dots[0][1])
    
    # 고정이 아니면
    # dots[0][0]과 dots[i][0]를 비교 다른거 찾기
    # dots[0][1]과 dots[i][1]를 비교 다른거 찾기

# max, min으로 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

# math 라이브러리 활용
import math

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def solution(dots):   
    A = dots.pop(0)
    for dot in dots:
        if A[0] == dot[0]:
            B = dot
        elif A[1] == dot[1]:
            C = dot

    return distance(*A, *B) * distance(*A, *C)

너무 어렵게 푼거 같다. math를 쓰면

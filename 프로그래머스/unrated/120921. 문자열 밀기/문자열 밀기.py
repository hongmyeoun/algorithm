def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]

    return -1

# insert와 pop을 이용한 방법
def solution(A, B):
    A, B = list(A), list(B)

    for i in range(len(A)):
        if A == B:
            return i
        A.insert(0, A.pop()) # 0번째 자리에 A.pop()을 넣기, pop()은 리스트의 끝 원소
        
    return -1

# deque 풀이
from collections import deque

def solution(A, B):
    A, B = deque(A), deque(B) # deque는 앞 뒤에서 데이터를 처리할 수 있는 양방향 자료형

    for i in range(len(A)):
        if A == B:
            return i
        A.rotate() # deque에 rotate() 기본값 1로 오른쪽으로 1칸 이동(양방향이므로 -1원소는 0으로간다.)
        
    return -1

# find로 풀이
def solution(A, B):
    BB = B*2
    return BB.find(A)

find는 그 값이 존재하는 index를 반환, 없다면 -1을 반환.

# 참고 풀이 https://codest.tistory.com/25

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    while A:
        max_A, max_B = A[-1], B[-1]
        min_A, min_B = A[0], B[0]
        AB, BA = max_A * min_B, max_B * min_A

        if AB < BA:
            answer += AB
            A.pop(-1)
            B.pop(0)
        else:
            answer += BA
            A.pop(0)
            B.pop(-1)
        
    return answer

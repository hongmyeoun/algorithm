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

고심끝에 나온 또다른 풀이
테스트 케이스
A = [1, 1, 4], B = [4, 1, 4]일때 결과를 잘못 계산해봐서 쉬운 문제를 어렵게 풀게됨...
결과로 12가 나오지만 10이라고 잘못계산함...

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    while A:        
        max_A, max_B = A[-1], B[-1]
        min_A, min_B = A[0], B[0]
        AB, BA = max_A * min_B, max_B * min_A

        if len(A) == 1:
            answer += AB
            break
        
        if AB < BA:
            answer += AB
            A.pop(-1)
            B.pop(0)
        elif AB > BA:
            answer += BA
            A.pop(0)
            B.pop(-1)
        else:
            for i in range(2, len(A)):
                if A[-i] * B[i-1] < B[-i] * A[i-1]:
                    answer += AB
                    A.pop(-1)
                    B.pop(0)
                    break
                elif A[-i] * B[i] > B[-i] * A[i]:
                    answer += BA
                    A.pop(0)
                    B.pop(-1)
                    break
                else:
                    answer += AB*len(A)
                    return answer

                    
    return answer

처음 생각했던 풀이
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

그냥 서로 반대로 정렬된 리스트를 곱하면 값이 나오겠거니 했었는데, 뭔가 아닐거 같아 안그랬다...
하지만 정답?

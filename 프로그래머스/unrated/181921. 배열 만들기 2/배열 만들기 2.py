def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        # num을 순회하면서 집합 {'0', '5'}와 같은 요소가 있는지 판단 all()은 반복문 전체를 뜻함(전체반복)
        if all(digit in {'0', '5'} for digit in str(num)):
            answer.append(num)
    if not answer:
        answer = [-1]
    return answer
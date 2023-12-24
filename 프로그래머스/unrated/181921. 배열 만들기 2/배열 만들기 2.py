def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        # num을 순회하면서 집합 {'0', '5'}와 같은 요소가 있는지 판단 all()은 반복문 전체를 뜻함(전체반복)
        if all(digit in {'0', '5'} for digit in str(num)):
            answer.append(num)
    if not answer:
        answer = [-1]
    return answer

# 차집합 이용
def solution(l, r):
    answer = []  # 결과를 저장할 리스트

    # 숫자 l부터 r까지 반복
    for num in range(l, r + 1):
        # 숫자를 문자열로 변환하여 집합으로 만들고, {'0', '5'}와의 차집합을 확인
        if not set(str(num)) - set(['0', '5']):
            # 차집합이 비어 있다면 (즉, 모든 자릿수가 '0' 또는 '5'인 경우)
            answer.append(num)  # 결과 리스트에 해당 숫자 추가

    # 만약 결과 리스트가 비어 있다면 -1을 담은 리스트를 반환, 아니면 결과 리스트를 반환
    return answer if answer else [-1]

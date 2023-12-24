def solution(a, b, c, d):
    num = [a, b, c, d]
    set_count = len(set(num))
    answer = 0
    # 4개의 숫자가 같을때
    # 1111 × p
    if set_count == 1:
        answer = 1111 * a

    # 3개가 같을때(set_count == 2)
    if set_count == 2:
    # 그 3개와 나머지 하나를 얻어야함
    # [a, b, c, d]에서 num.count가 3이면 p, 1이면 q
    # (10 × p + q)2
    # 2개가 같을때(set_count == 2)
    # 둘 둘 짝이 지어졌을때(two_two)
    # (p + q) × |p - q|
        p = 0
        q = 0
        two_two = []
        for element in set(num):
            if num.count(element) == 3:
                p = element
            elif num.count(element) == 1:
                q = element

            elif num.count(element) == 2:
                two_two.append(element)

        if not two_two:
            answer = (10 * p + q) ** 2
        else:
            answer = (two_two[0] + two_two[1]) * abs(two_two[0] - two_two[1])

    # 짝이 하나만 있을때(나머지 q, r) (set_count == 3)
    if set_count == 3:
        q_r = []
        for element in set(num):
            if num.count(element) == 1:
                q_r.append(element)
    # q × r
        answer = q_r[0] * q_r[1]

    # 다 다를때
    if set_count == 4:
    # 가장 작은수
        answer = min(num)
    return answer

def solution(citations):
    answer = 0
    test = []
    count = 0
    h_idx = 0
    for i in citations:
        for j in citations:
            if i <= j:
                count += 1
        h_idx = min(count, i)
        if h_idx >= answer:
            answer = h_idx
            test.append(answer)
        count = 0
    return answer
# 인용 횟수 vs 인용 횟수이상의 논문의 수
# 에서 더 작은 수가 h-index

# [10, 8, 5, 4, 3] 의 인용횟수를 가진 교수가 있다면
# 10번 이상 인용 횟수를 가진 논문은 1편입니다. 이때 H-Index는 1입니다.
# 8번 이상 인용 횟수를 가진 논문은 2편입니다. 이때 H-Index는 2입니다.
# 5번 이상 인용 횟수를 가진 논문은 3편입니다. 이때 H-Index는 3입니다.
# 4번 이상 인용 횟수를 가진 논문은 4편입니다. 이때 H-Index는 4입니다.
# 3번 이상 인용 횟수를 가진 논문은 5편입니다. 이때 H-Index는 3입니다.
# 여기서 H-Index는 4입니다 이 경우에는 논문의 개수와 인용 횟수가 같으니 헷갈리실수 있습니다.

# [9, 7, 6, 2, 1] 의 인용횟수를 가진 교수가 있다면
# 9번 이상 인용 횟수를 가진 논문은 1편입니다. 이때 H-Index는 1입니다.
# 7번 이상 인용 횟수를 가진 논문은 2편입니다. 이때 H-Index는 2입니다.
# 6번 이상 인용 횟수를 가진 논문은 3편입니다. 이때 H-Index는 3입니다.
# 2번 이상 인용 횟수를 가진 논문은 4편입니다. 이때 H-Index는 2입니다.
# 1번 이상 인용 횟수를 가진 논문은 5편입니다. 이때 H-Index는 1입니다.
# 여기서 H-Index는 3입니다.

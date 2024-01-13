def solution(k, score):
    answer = []
    fame = []
    for i in score:
        if len(fame) > k-1:
            if i >= min(fame):
                fame.remove(min(fame))
                fame.append(i)
        else:
            fame.append(i)
        answer.append(min(fame))
    return answer

# k크기의 list에 score를 추가
# 하지만 k의 가장 낮은 점수보다 낮으면 추가 X
# 매 회 있는 k에 min값 append
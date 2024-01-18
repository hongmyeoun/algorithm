def solution(participant, completion):
    answer = ''
    dict_participant = {}
    participant
    for idx, person in enumerate(participant):
        if person not in dict_participant:
            dict_participant[person] = [idx]
        else:
            dict_participant[person].append(idx)
            
    for person in completion:
        if person in dict_participant and dict_participant[person]:
            dict_participant[person].pop()
            
    for key, value in dict_participant.items():
        if value:
            answer = key
    
    return answer

# dict으로 참가자의 인덱스를 저장
# 완주자 이름과 비교하며 인덱스를 하나씩 빼냄
# 순회를 맞췄을때 인덱스가 남아있는 dict의 key를 반환


# collections의 counter 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

Counter는 리스트나 문자열에 대해서 요소의 개수를 셈
이때 서로 계산을 할 수 있는데, 위 식에서 '-'를 하게 되면, 각 key 끼리 value의 '-' 계산
결론적으로 겹치는 요소는 삭제
남은 요소가 마지막 주자

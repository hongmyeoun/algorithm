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
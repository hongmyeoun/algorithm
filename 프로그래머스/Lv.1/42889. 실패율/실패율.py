def solution(N, stages):
    stage_fail = {}
    c = len(stages)
    
    for i in range(1, N+1):
        if c != 0:
            f = stages.count(i)
            stage_fail[i] = f/c
            c -= f
            
        else:
            stage_fail[i] = 0
    
    return sorted(stage_fail, key=lambda i: stage_fail[i], reverse=True)
    
# 스테이지 실패율을 딕셔너리에 저장
# 성공자가 있다면
# 실패자/성공자
# 실패자는 1부터 N까지 순회를 할때 i값의 수
# 성공자는 남아있는 stages길이
# 실패율을 계산하고 나면, 성공자에서 실패자를 뺌
# 도전자가 0이면 실패율은 0


# 첫 도전

# def solution(N, stages):
#     answer = []
#     sorted_stages = sorted(stages)
    
#     for i in range(1, N+1):
#         if not sorted_stages:
#             break
            
#         count = sorted_stages.count(i)
#         answer.append(count/len(sorted_stages))
#         sorted_stages = [j for j in sorted_stages if j != i]
    
#     answer = sorted(range(len(answer)), key=lambda i: answer[i], reverse=True)
#     return [i+1 for i in answer]


# 실패율을 구하는 코드
# 실패율 == 스테이지에 도달했으나, 아직 클리허지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# N : 전체 스테이지의 개수, N+1의 요소는 성공자이므로 
# stages : 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열

# return 실패율이 높은 스테이지부터 내림차순으로

# 스테이지에 도달한 유저가 없으면 해당 스테이지 실패율은 0

# 실패율을 계산한 후 모든 요소 삭제
# 실패율과 인덱스를 정렬한값 + 1 반환

# 첫 도전방식은
# 입력값 〉	2, [1, 1, 1, 1]
# 기댓값 〉	[1, 2]
# 이 반례를 해결하지 못했다.
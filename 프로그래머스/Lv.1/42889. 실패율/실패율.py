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


# 첫 풀이
def solution(N, stages):
    answer = []
    sorted_stages = sorted(stages)
    
    for i in range(1, N+1):
        if not sorted_stages:
            break
            
        count = sorted_stages.count(i)
        answer.append(count/len(sorted_stages))
        sorted_stages = [j for j in sorted_stages if j != i]
    
    answer = sorted(range(len(answer)), key=lambda i: answer[i], reverse=True)
    return [i+1 for i in answer]
# 실패율을 구하는 코드
# 실패율 == 스테이지에 도달했으나, 아직 클리허지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# N : 전체 스테이지의 개수, N+1의 요소는 성공자이므로 
# stages : 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열

# return 실패율이 높은 스테이지부터 내림차순으로

# 스테이지에 도달한 유저가 없으면 해당 스테이지 실패율은 0

# 실패율을 계산한 후 모든 요소 삭제
# 실패율과 인덱스를 정렬한값 + 1 반환

첫 도전방식은
입력값 〉	2, [1, 1, 1, 1]
기댓값 〉	[1, 2]
이 반례를 해결하지 못했다.

# 해쉬 테이블 방식
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):]) # 실패율이 0일경우
        yet = info[i + 1] # 해당 스테이지에 머물러 있는 사람
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer

주어진 코드에서 해시 테이블의 역할은 각 스테이지에 머물러 있는 플레이어의 수를 효율적으로 계산하기 위함입니다.

info 리스트: 각 스테이지에서 머물러 있는 플레이어의 수를 나타냅니다. 
스테이지 번호가 인덱스로 사용되고, 해당 스테이지에 머무르는 플레이어 수가 값으로 저장됩니다.
for stage in stages: info[stage] += 1: 
주어진 스테이지 리스트를 순회하면서 각 스테이지에 머물러 있는 플레이어 수를 계산하고, info 리스트에 반영합니다.


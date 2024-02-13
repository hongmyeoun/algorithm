def solution(priorities, location):
    priorities_with_idx = [[priorities[i], i] for i in range(len(priorities))]
    process_idx = []
    
    while True:
        process_index = 0
        
        if not priorities_with_idx:
            break
        
        check_max = [i[0] for i in priorities_with_idx]
        
        if priorities_with_idx[process_index][process_index] < max(check_max):
            priorities_with_idx.append(priorities_with_idx.pop(process_index))
        else:
            process_idx.append(priorities_with_idx.pop(process_index))
        
    
    process_idx = [i[-1] for i in process_idx]
    return process_idx.index(location)+1

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 우선도만 같으면 됨
    
# [A:2, B:1, C:3, D:2]
# 0: [A,B,C,D]
# 1: [B,C,D] -> [B,C,D,A]
# 2: [C,D,A] -> [C,D,A,B]
# 3: [C,D,A,B] == [3,2,2,1]

# 비슷한 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # any() 인자로 받은 iterable(순회 가능한 객체)의 요소 중에서 어느 하나라도 조건을 만족하는지 검사 => 만족 True, ㄴ False
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# deque를 사용
from collections import deque
def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    maximum = max(priorities)
    answer = 0
    while True:
        index = index_list.popleft()
        if priorities[index] < maximum:
            index_list.append(index)
        else:
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            if index == location:
                return answer

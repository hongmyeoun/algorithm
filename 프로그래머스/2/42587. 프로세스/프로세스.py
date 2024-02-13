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
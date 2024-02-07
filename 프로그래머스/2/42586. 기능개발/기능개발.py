def solution(progresses, speeds):
    answer = []
    remain = []
    for idx, (progress, speed) in enumerate(zip(progresses, speeds)):
        if (100-progress)%speed != 0:
            remain.append((100-progress)//speed+1)
        else:
            remain.append((100-progress)//speed)
    
    temp = 1
    max_num = remain[0]
    for i in range(len(remain)-1):
        if remain[i+1] <= max_num:
            temp += 1
        else:
            max_num = remain[i+1]
            answer.append(temp)
            temp = 1
    
    answer.append(temp)
    
    return answer

# 뒤에 있는 기능은 앞에 있는 기능의 개발이 끝나야 배포 가능
# 각 배포마다 몇번의 기능이 배포되는지 

# (100 - progresses[i]) // speeds[i] -> 남은 개발 일정
# 남은 개발 일정을 순회하면서
# 가장 큰값(초기엔 0번째)을 저장하고
# 다음 요소가 그것 보다 작거나 같으면 temp(초기값 1) 에 1을 더함
# 그렇지 않으면 그 값을 가장 큰값으로 저장
# 그리고 temp값을 answer에 append

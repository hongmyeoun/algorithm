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

# pop()을 이용한 풀이
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

# progress를 제거해나가면서 값을 추가하는 방식

# progresses가 남아있을동안 반복
# 만약 진행도가 100이 안됐다면(현재 진행도 + 시간에 따른 진행도) >= 0
# 시간을 하루 추가
# 배포카운터가 0보다 클경우(배포된 것이 있다면)
# 배포카운터를 answer에 추가
# 100이상이면
# 가장 앞 작업, speed를 제거(배포)
# 배포 카운트 +1

# progresses가 모두 제거되었다면
# 남은 배포카운터를 answer에 추가

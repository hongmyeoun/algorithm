def solution(k, m, score):
    answer = []
    score.sort(reverse=True)
    for i in range(0, len(score)+1, m):
        if len(score[i:i+m]) == m:
            answer.append(min(score[i:i+m])*len(score[i:i+m]))
    return sum(answer)

# m = 한 상자에 들어갈 사과의 개수
# k = 최대 점수

# 몇상자를 팔 수 있나 -> len(score)//m 12//3 -> 4

# score를 큰 순으로 정렬, 상자길이로 짤라감 안남을때까지 반복

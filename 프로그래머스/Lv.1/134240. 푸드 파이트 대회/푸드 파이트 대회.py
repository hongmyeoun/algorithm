def solution(food):
    front = ''
    for idx, i in enumerate(food):
        if idx == 0:
            pass
        elif i%2 == 1:
            front = front + f'{idx}'*((i-1)//2)
        elif i%2 == 0:
            front = front + f'{idx}'*(i//2)
    
    return front + '0' + front[::-1]

# 각 음식이 홀수면 -1만큼 반을 나눠서 숫자를 넣음
# 3이 다 들어갔으면

# 양옆으로 중앙에서부터 채우는 방식
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer

# 나랑 똑같지마 조건문이 줄어드는 방식
def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]

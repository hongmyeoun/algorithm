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
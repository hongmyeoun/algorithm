def solution(num_list):
    answer = 0
    for i in num_list:
        temp = i
        while temp != 1:
            if temp % 2: # 홀수이면
                temp = (temp-1)//2
                answer += 1
            else:
                temp //= 2
                answer += 1
    return answer
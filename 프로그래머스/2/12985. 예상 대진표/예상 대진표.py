def solution(n,a,b):
    answer = 0
    while True:
        # if (a+1 == b or b+1 == a) and (min(a, b)%2 == 1):
        if (min(a, b)+1 == max(a, b)) and (min(a, b)%2 == 1):
            answer += 1
            break
        a = next_round(a)
        b = next_round(b)
        answer += 1
        
    return answer

def next_round(a):
    if a%2==0:
        a //= 2
    else:
        a = a//2 + a%2

    return a
# 홀수 -> 1이면 1, 3이면 2, 5이면 3
# 짝수 -> 2이면 1, 4이면 2, 6이면 3
# -> 1 또는 2가 될때 까지 반복

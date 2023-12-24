def solution(n):
    answer = [n]
    while n != 1:
        n = n // 2 if not n % 2 else 3 * n + 1
        answer.append(n)
    return answer

# 처음에 나는 /로 나눗셈을 했지만 //가 몫을 가져가는 것이므로 // 사용해야됨
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer

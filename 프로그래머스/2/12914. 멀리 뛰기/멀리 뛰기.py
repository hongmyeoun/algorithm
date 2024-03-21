def solution(n):
    return fibo(n)%1234567

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        pre, nex = 1, 2
        for i in range(n-2):
            pre, nex = nex, pre + nex
        return nex

# 한칸 또는 두칸밖에 못뜀
# 4라면 4를 2로 나눈수 2 == 2를 최대 몇번 사용하는지 알려줌
# 0번 -> 1개
# 1번 -> n-1개
# 2번 -> n-2개
# ...
# n/2 -> 1개
# 홀수이면 n/2 1개를 빼야함 
# -> 5부터 불가능

# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8
# 6 = 13
# -> 피보나치?
# Fn = Fn-1 + Fn-2
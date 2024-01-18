def solution(n):
    n_2 = 0
    n_1 = 1
    
    for i in range(2,n+1):
        n_1, n_2 = n_1+n_2, n_1
    return n_1%1234567

# def fibo(n):
#     if n <= 1:
#         return n
    
#     return fibo(n-1) + fibo(n-2)

# 피보나치 수열
# 0으로 시작
# 1을 더함
# 이후부터는 이전 두 값을 더한값
# 0, 1, 1, 2, 3, 5, 8
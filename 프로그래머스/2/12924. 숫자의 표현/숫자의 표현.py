def solution(n):
    result = 0
    i = 1
    while i <= n:
        total = 0
        j = i
        while total < n:
            total += j
            j += 1
        if total == n:
            result += 1
        i += 1
    return result


# def solution(n):
#     result = 0
#     i = 1
#     while i<=n:
#         if (n - i)%i == 0:
#             result += 1
#         i += 1
#     return result

# 15 - 1 = 14
# 14//1 = 14, 14%1 = 0
# 1+14
# 15 - (1 + 2) = 12
# 12//2 = 6, 12%2 = 0
# 6+1 + 6+2 = 15
# 15 - (1+2+3) = 9
# 9//3 = 3, 9%3 = 0
# 3+1 + 3+2 + 3+3 = 15
# 15 - (1+2+3+4) = 5
# 5%4 = 1
# 15 - (1+2+3+4+5) = 0
# 0%5 = 0, 0//5 = 0

# 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

def expressions(num):
    answer = 0
    for i in range(1, num+1):
        summ = 0
        while (summ < num):
            summ += i
            i += 1
        if summ == num:
            answer += 1
    return answer

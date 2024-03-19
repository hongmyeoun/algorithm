import math

def solution(arr):
    answer = 0
    
    for i in range(len(arr)-1):
        if i == 0:
            answer = lcm(arr[i], arr[i+1])
        else:
            answer = lcm(answer, arr[i+1])
    
    return answer

def lcm(a, b):
    return a * b // math.gcd(a, b)

더 간단히
def solution(arr):
    answer = arr[0]
    
    for num in arr:
        answer = num * answer // math.gcd(num, answer)
    
    return answer

fraction이라는 것 까먹지 말기

from fractions import gcd

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

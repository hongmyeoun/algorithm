def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    
    result = 1
    for i in num_list:
        result *= i
        
    return result

# 라이브러리 사용 prod
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)

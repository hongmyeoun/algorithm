def solution(num_list):
    result = 1
    for i in num_list:
        result *= i
    
    if result < sum(num_list)**2:
        return 1
    else:
        return 0

# import math를 활용
import math
def solution(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list)**2):
        answer = 1
    return answer

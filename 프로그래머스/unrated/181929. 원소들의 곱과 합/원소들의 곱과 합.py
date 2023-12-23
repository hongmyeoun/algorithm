def solution(num_list):
    result = 1
    for i in num_list:
        result *= i
    
    if result < sum(num_list)**2:
        return 1
    else:
        return 0
    
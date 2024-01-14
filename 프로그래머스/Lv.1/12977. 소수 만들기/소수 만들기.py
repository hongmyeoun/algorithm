from itertools import combinations

def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)):
        if all(sum(i)%j != 0 for j in range(2, sum(i))):
            answer += 1
    
    return answer
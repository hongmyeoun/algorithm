from itertools import combinations

def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)):
        if all(sum(i)%j != 0 for j in range(2, sum(i))):
            answer += 1
    
    return answer

# 에라스토테네스의 체를 이용한 소수 처리
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1): # 제곱근 이하까지의 배수를 삭제하는 방식
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])

def solution(nums):
    return min(len(set(nums)), len(nums)//2)

# 중복을 허용하게 됐을때, 종류가 반을 나눈거보다 많다면 그냥 반나눈거만큼 가져가는게 이득
# 아니면 중복된애들을 최소한으로 가져가기

# 문제를 잘못봄...조합을 찾는건줄
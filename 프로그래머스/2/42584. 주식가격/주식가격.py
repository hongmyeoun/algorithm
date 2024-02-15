def solution(prices):
    stack = []
    time = [0]*len(prices)
    for i in range(len(prices)):
        for _, idx in stack:
            time[idx] += 1
        while stack:
            if stack[-1][0] > prices[i]:
                stack.pop()
            else:
                break
        stack.append((prices[i],i))    
    return time

# stack에 가격과 인덱스를 넣어줌
# stack안에 값이 존재할 동안
# 그 stack에 들어온 값과 현재 가격을 비교
# 만약 stack에 들어온 값이 더 크다면
# stack.pop()

# 더 작다면
# stack break
# stack의 1번째 요소를 순회(prices의 인덱스)
# 0으로 채워진 prices와 같은 크기의 리스트 time에 index 값을 증가시킴

# 제출을 못함(대부분 틀림)
# def solution(prices):
#     answer = []
#     for idx, i in enumerate(prices):
#         if idx == len(prices) - 1:
#             answer.append(0)
#         elif min(prices[idx:]) == i:
#             answer.append(len(prices[idx:])-1)
#         elif prices[idx+1] < i:
#             answer.append(1)
#     return answer

# [1,2,3,2,3] -> [2,3,2,3] [(1,0)]
# [2,3,2,3] -> [3,2,3] [(1,1),(2,0)]
# [3,2,3] -> [2,3] [(1,2),(2,1),(3,0)]
# [2,3] -> [3] [(1,3),(2,2),(3,1),(2,0)]
# [3] -> [] [(1,4),(2,3),(3,1),(2,1),(3,0)]
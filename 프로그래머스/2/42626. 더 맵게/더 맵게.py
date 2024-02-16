import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 우선순위 큐로 변환(최소힙 형태)
    while True:
        if scoville[0] >= K:  # 가장 작은 스코빌 지수가 K 이상이면 종료
            break
        if len(scoville) < 2:  # 스코빌 지수를 만들 수 없는 경우
            return -1
        # 가장 작은 두 개의 음식을 꺼내서 섞음
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)  # 섞은 음식을 다시 우선순위 큐에 넣음
        answer += 1
    return answer

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# k이하인 스코빌 지수를 갖은 음식 둘을 섞음

# 처음에 짠 코드
# def solution(scoville, K):
#     answer = 0
#     scoville = list(filter(lambda x: x < K, scoville)) # [1,2,3]
#     while True:
#         scoville.sort() # [1,2,3]
#         one, two = scoville[0], scoville[1] # one=1, two=2
#         if one < K and two < K: # 1<7 true, 2<7 true
#             scoville[1] = one + (two*2) # [1,5,3]
#             answer += 1
#             if len(scoville) > 2:
#                 scoville.pop(0) # [5,3]
#             else:
#                 break
            
#     return scoville
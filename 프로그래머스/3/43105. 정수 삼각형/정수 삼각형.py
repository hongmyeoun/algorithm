def solution(triangle):
    # 맨 위층부터 아래층으로 내려가면서 최대값을 계산하고 저장
    for i in range(1, len(triangle)):  # 맨 위층은 제외하고 시작
        for j in range(len(triangle[i])):
            # 현재 층의 각 요소는 이전 층의 해당 위치와 그 전 위치의 값 중 큰 값과 현재 층의 값과 더해짐
            if j == 0:  # 왼쪽 끝 요소는 바로 위의 값만 고려
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:  # 오른쪽 끝 요소는 바로 위의 값만 고려
                triangle[i][j] += triangle[i - 1][j - 1]
            else:  # 그 외의 요소는 바로 위의 값 둘 중 큰 값과 더해짐
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    # 맨 아래층의 최대값 반환
    return max(triangle[-1])

# 1층과 2층을 더해서 2층에 저장(최대값을)
# 7
# 3 8 -> 10 15
# 2층과 3층을 더해서 3층에 저장(최대값을)
# 10 15
# 8 1 0 -> 18 11/16 15 -> 18 16 15
# 3층과 4층을 더해서 4층에 저장(최대값을)
# 18 16 15
# 2 7 4 4 -> 20 25/23 20/19 19 -> 20 25 20 19
# 4층과 5층을 더해서 5층에 저장(최대값을)
# 20 25 20 19
# 4 5 2 6 5 -> 24 25/30 27/22 26/25 24 -> 24 30 27 26 24
# 마지막 층에서 최대값 반환
# -> 30

# 다른사람의 dp식
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1): # 어쩌피 삼각형은 하나씩 커지니깐 triangle의 길이를 재지 않아도 됨
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])

# ????????
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
설명
1. 한 층씩 제거하며, 그 층에서 계산한 최대 이동거리 배열을 계산하여, 한 층을 제거한 traingle을 첫번째 input, 이동거리 배열을 두 번째 input으로 넣어줍니다.
2. 따라서 traingle이 없으면 제거할 층이 없으므로 최종 조건입니다. 
3. [0] + l, l + [0] 을 이용하여 모서리 조건을 해결해줍니다.
-> 위 두식과 비슷한듯??

# 반대로 올라가는 식
def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1): # 밑에서부터 위로 올라감, range(start, end, step) end = -1 ==> 0
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


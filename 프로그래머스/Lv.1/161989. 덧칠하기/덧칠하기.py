def solution(n, m, section):
    answer = 0
    wall = [1 for _ in range(n)]
    for i in section:
        wall[i-1] = 0
    
    i = 0
    while i < len(wall):
        if not wall[i]:
            end = min(i+m-1, len(wall)-1)
            
            for j in range(i, end+1):
                wall[j] = 1
            
            answer += 1
            i = end + 1
        else:
            i += 1
    
    return answer

# 페인트 한 번 칠하는 규칙
# - 롤러가 벽에서 벗어나면 안됨
# - 구역의 일부분만 포함되면 안됨

# n : 벽의 개수
# m : 한번에 칠할 수 있는 길이
# section : 빈곳(칠해야 하는 구역)

# 최소한의 페인트를 칠해 빈곳을 다 채우는 방법을 찾기

# 길이가 n짜리인 1로 채워진 리스트를 만듦
# 그 리스트를 순회하면서 0인부분을 찾음
# 0인 부분에서부터 index+m-1까지 1로 바꿔줌
# index+m-1부분과 len를 비교해 out of index 방지
# 바꾼뒤 count + 1
# 다음 순회는 end + 1로 조절

# 간단하게 풀이 리스트를 안만들어 효율적
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer

section과 section사이의 거리를 재서 그 거리가 m보다 크거나 같다면 색을 칠함
아니면 칠하지 않고 1을 반환

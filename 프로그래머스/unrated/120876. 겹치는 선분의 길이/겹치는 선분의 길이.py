def solution(lines):
    answer = set()
    for idx, line_first in enumerate(lines):
        for line_second in lines[idx+1:]:
            answer = answer | set(range(line_first[0],line_first[1])) & set(range(line_second[0],line_second[1]))
    return len(answer)

# 맨처음 line그니까 이전 line과 이후 line을 비교하며 교집합 구하기
# 교집합을 계속 합함

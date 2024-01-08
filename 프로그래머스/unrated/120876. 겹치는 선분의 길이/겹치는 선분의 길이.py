def solution(lines):
    answer = set()
    for idx, line_first in enumerate(lines):
        for line_second in lines[idx+1:]:
            answer = answer | set(range(line_first[0],line_first[1])) & set(range(line_second[0],line_second[1]))
    return len(answer)

# 맨처음 line그니까 이전 line과 이후 line을 비교하며 교집합 구하기
# 교집합을 계속 합함

# lines의 길이가 3이니까 할 수 있는 방법
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

sets에 lines의 최대값부터 최소값까지 set을 만들어 리스트로 저장
그 값은 3개가 나올거임
그래서 첫값, 두번째값 의 교집합, 둘째 셋째의 교집합, 셋째 첫쨰의 교집합을 합집합한 값 출력
-> line갯수 제한없어지면 풀수 없어짐

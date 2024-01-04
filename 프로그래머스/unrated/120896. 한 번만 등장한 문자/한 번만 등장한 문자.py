def solution(s):
    answer = ''
    for c in s:
        if s.count(c) == 1:
            answer += c
    return ''.join(sorted(answer))


# 같은 식
def solution(s):
    return "".join(sorted([ch for ch in s if s.count(ch) == 1]))

효율적으로 하려면 for문 횟수를 줄이기 위해 for c in s를 for c in set(s)로 바꿔준다

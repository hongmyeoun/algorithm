def solution(t, p):
    answer = 0
    for i in [int(t[i:len(p)+i]) for i in range(0, len(t)-(len(p)-1))]:
        if i <= int(p):
            answer += 1
    return answer

# 숏코딩 햄스터
def solution(t, p):
    return sum(1 for i in [int(t[i:len(p)+i]) for i in range(0, len(t)-(len(p)-1))] if i <= int(p))

# 더 간단한 풀이
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

그냥 저렇게 하면 될것을 list를 만드는 풀이를 왜 했을까

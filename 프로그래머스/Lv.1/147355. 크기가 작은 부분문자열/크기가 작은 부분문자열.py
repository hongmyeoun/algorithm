# def solution(t, p):
#     answer = 0
#     for i in [int(t[i:len(p)+i]) for i in range(0, len(t)-(len(p)-1))]:
#         if i <= int(p):
#             answer += 1
#     return answer

def solution(t, p):
    return sum(1 for i in [int(t[i:len(p)+i]) for i in range(0, len(t)-(len(p)-1))] if i <= int(p))
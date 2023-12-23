# 처음 풀이
# def solution(numLog):
#     answer = ''
#     key = dict(zip([1,-1,10,-10],['w','s','d','a']))
#     for i in range(len(numLog)):
#         if i < len(numLog) - 1:
#             key_num = numLog[i+1] - numLog[i]
#             answer += key[key_num]
#     return answer

def solution(numLog):
    answer = ''
    key = dict(zip([1,-1,10,-10],['w','s','d','a']))
    return ''.join([answer + key[next - current] for current, next in zip(numLog, numLog[1:])])

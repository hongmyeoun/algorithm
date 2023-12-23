# 처음 풀이
def solution(numLog):
    answer = ''
    key = dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(len(numLog)):
        if i < len(numLog) - 1:
            key_num = numLog[i+1] - numLog[i]
            answer += key[key_num]
    return answer

# 더 간결화 해봤음
def solution(numLog):
    answer = ''
    key = dict(zip([1,-1,10,-10],['w','s','d','a']))
    return ''.join([answer + key[next - current] for current, next in zip(numLog, numLog[1:])])

# 다른사람 풀이
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

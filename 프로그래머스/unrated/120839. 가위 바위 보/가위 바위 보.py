def solution(rsp):
    answer = ''
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    for c in rsp:
        if c == '2':
            answer += rsp_dict[c]
        elif c == '0':
            answer += rsp_dict[c]
        elif c == '5':
            answer += rsp_dict[c]
    return answer

# 더 쉽게 사용
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

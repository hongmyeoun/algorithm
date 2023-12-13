def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            ineq_bool = n >= m
        elif eq == "!":
            ineq_bool = n > m
    elif ineq == "<":
        if eq == "=":
            ineq_bool = n <= m
        elif eq == "!":
            ineq_bool = n < m
    
    answer = 1 if ineq_bool else 0
    
    return answer

# 다른사람 풀이
def solution(ineq, eq, n, m):
    # eval은 파이썬 표현식으로 평가하는 함수
    # ex) answer = eval("2+5") // answer == 7 -> type == any
    # 타입이 any이므로 int를 취해준다.
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n} {ineq}{eq} {m}'))

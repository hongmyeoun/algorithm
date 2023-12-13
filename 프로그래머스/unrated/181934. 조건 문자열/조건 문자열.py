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
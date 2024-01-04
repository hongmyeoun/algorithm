def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0,len(my_str)+1,n)]
    return [c for c in answer if c != '']
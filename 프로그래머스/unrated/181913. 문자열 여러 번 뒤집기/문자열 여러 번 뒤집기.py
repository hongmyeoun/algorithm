def solution(my_string, queries):
    my_string = list(my_string)
    for s, e in  queries:
        my_string[s:e + 1] = list(reversed(my_string[s:e + 1]))
    return ''.join(my_string)

# [::1] 을 통해 reverse
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)

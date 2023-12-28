solution = lambda my_string, s, e: my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]

# list로 변환후 reversed -> 
def solution(my_string, s, e):
    substr = reversed(list(my_string[s:e+1])) # list(my_string[s:e+1])[::-1] 과 동일
    return my_string[:s] + ''.join(substr) + my_string[e+1:]

def solution(my_string, alp):
    for c in my_string:
        if c == alp:
            my_string = my_string.replace(c, c.upper())
    return my_string

# 그냥 이렇게 하면된다...
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

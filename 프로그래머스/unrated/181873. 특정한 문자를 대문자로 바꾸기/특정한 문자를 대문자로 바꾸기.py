def solution(my_string, alp):
    for c in my_string:
        if c == alp:
            my_string = my_string.replace(c, c.upper())
    return my_string
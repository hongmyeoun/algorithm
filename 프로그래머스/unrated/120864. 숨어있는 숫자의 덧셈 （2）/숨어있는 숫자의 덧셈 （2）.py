def solution(my_string):
    for c in my_string:
        if not c.isdigit():
            my_string = my_string.replace(c, " ")
            
    my_string = my_string.split()
    
    return sum(int(i) for i in my_string)

# 위 식을 간단히 하면
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

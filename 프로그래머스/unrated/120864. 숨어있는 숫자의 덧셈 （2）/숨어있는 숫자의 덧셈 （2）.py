def solution(my_string):
    for c in my_string:
        if not c.isdigit():
            my_string = my_string.replace(c, " ")
            
    my_string = my_string.split()
    
    return sum(int(i) for i in my_string)
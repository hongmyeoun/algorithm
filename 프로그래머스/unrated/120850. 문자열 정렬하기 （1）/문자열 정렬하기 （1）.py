def solution(my_string):
    num = ['0','1','2','3','4','5','6','7','8','9']
    return sorted([int(c) for c in my_string if c in num])
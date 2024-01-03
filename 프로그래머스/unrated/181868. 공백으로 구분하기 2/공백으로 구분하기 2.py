def solution(my_string):
    return [c for c in my_string.split(' ') if c != '']
    
# 공백 한정으로는 split()을 하면 중복되는 것도 지워줌
solution=lambda x:x.split()

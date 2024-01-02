def solution(my_string):
    for c in ['a','e','i','o','u']:
        my_string = my_string.replace(c, '')
    return my_string

# 숏코딩 힙스터
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

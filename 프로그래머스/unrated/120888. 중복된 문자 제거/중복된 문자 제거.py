def solution(my_string):
    result = []
    for c in my_string:
        if c not in result:
            result.append(c)
    return ''.join(result)

# 키로 만들어서 중복 제거
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

제거후 다시 키값을 붙임

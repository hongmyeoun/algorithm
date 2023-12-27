def solution(my_string, is_suffix):
    my_string_suffix = [my_string[-i:] for i in range(len(my_string))]
    return 1 if is_suffix in my_string_suffix else 0

# 다른 풀이 1
is_suffix도 결국엔 접미사를 넣어주는거기 때문에 my_string에 뒷부분에 넣어주고 비교만 하면된다.
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix: return 1
    return 0

# endwith()를 사용한 풀이
str.endwith(suffix)는 문자열이 주어진 접미사로 끝나면 True, 아니면 False를 반환하는 함수
int()는 True는 1 False는 0으로 반환하는 함수
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

solution = lambda my_string, is_prefix: int(my_string[:len(is_prefix)] == is_prefix)

# startwith()도 있음... 왜 자동완성에 안나왔지?
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

lambda my_string, is_prefix: int(my_string.startswith(is_prefix))

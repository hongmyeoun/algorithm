def solution(my_string, is_suffix):
    my_string_suffix = [my_string[-i:] for i in range(len(my_string))]
    return 1 if is_suffix in my_string_suffix else 0
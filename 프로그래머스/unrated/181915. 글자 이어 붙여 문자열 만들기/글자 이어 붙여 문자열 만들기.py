def solution(my_string, index_list):
    # my_string의 len만큼 dict 하고싶음
    answer = ''
    dic_str = dict(zip(list(range(0, len(my_string))), [c for c in my_string]))
    return ''.join([answer + dic_str[idx] for idx in index_list])
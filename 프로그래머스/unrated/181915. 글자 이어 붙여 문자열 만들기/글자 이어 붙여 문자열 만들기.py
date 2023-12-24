def solution(my_string, index_list):
    # my_string의 len만큼 dict 하고싶음
    answer = ''
    dic_str = dict(zip(list(range(0, len(my_string))), [c for c in my_string]))
    return ''.join([answer + dic_str[idx] for idx in index_list])

# 너무 어렵게 생각했고, 그냥 str의 인덱스값을 불러오면됨...
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

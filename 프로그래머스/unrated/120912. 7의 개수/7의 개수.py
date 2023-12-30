def solution(array):
    str_array = [str(i) for i in array]
    num_str = ''.join(str_array)
    return num_str.count('7')
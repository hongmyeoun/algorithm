def solution(num_list):
    last = num_list[len(num_list) - 1]
    before_last = num_list[len(num_list) - 2]
    if last > before_last:
        num_list.append(last - before_last)
    else:
        num_list.append(last*2)
    return num_list
def solution(num_list):
    last = num_list[len(num_list) - 1]
    before_last = num_list[len(num_list) - 2]
    if last > before_last:
        num_list.append(last - before_last)
    else:
        num_list.append(last*2)
    return num_list

# python에서 list의 순서는 -1 이 있었다는거 까먹어서 못햇던것
def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l

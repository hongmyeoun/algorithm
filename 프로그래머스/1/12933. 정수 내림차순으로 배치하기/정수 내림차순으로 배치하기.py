def solution(n):
    num_list = [int(i) for i in str(n)]
    num_list.sort(reverse=True)
    return int(''.join([str(i) for i in num_list]))
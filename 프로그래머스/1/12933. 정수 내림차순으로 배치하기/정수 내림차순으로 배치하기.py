def solution(n):
    num_list = [int(i) for i in str(n)]
    num_list.sort(reverse=True)
    return int(''.join([str(i) for i in num_list]))

# 같은 식 간단하게
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

정수를 list하면 나눠져서 들어간다

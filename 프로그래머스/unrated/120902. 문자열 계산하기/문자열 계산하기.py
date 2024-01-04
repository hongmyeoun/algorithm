def solution(my_string):
    return eval(my_string)

# -를 + -로 바꾸고 전부 더함
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

def solution(my_string, indices):
    my_string = [c for c in my_string]
    for i in indices:
        my_string[i] = ''
    return ''.join(my_string)

# not 사용
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer

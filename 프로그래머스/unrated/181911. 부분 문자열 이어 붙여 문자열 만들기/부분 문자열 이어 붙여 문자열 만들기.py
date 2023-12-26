def solution(my_strings, parts):
    return ''.join([my_strings[i][parts[i][0]:parts[i][1] + 1] for i in range(0, len(my_strings))])

# zip 풀이가 더 간단한거 같음 방법은 동일
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])

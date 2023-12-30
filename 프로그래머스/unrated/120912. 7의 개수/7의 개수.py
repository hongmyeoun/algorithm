def solution(array):
    str_array = [str(i) for i in array]
    num_str = ''.join(str_array)
    return num_str.count('7')

문제를 풀기전에 array 전체를 str로 못바꾸나? 생각하면서 일단 순회를 돌리기로 했음
그리고 str.count(X) 가 되는 것을 알았음

# 다른 사람 풀이
def solution(array):
    return str(array).count('7')

이 풀이를 보고, list를 str로 그냥 바꿀수 있다는 것을 깨달음

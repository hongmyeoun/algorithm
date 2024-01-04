def solution(array, n):
    close = abs(max(array) - n)
    result = max(array)
    array.sort(reverse=True)
    for i in array:
        if close >= abs(i-n):
            close = abs(i-n)
            result = i
    return result


# 간단하게
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer

그냥 정렬을 n과의 거리순으로 하면 되는거였음 ㅠㅠ

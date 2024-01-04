def solution(array, n):
    close = abs(max(array) - n)
    result = max(array)
    array.sort(reverse=True)
    for i in array:
        if close >= abs(i-n):
            close = abs(i-n)
            result = i
    return result
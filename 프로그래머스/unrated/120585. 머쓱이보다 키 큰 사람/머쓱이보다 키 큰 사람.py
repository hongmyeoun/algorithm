def solution(array, height):
    array.append(height)
    array.sort()
    array = array[::-1]
    return array.index(height)

def solution(array, height):
    array.append(height)
    array.sort(reverse=True) # reverse 파라미터가 있음
    return array.index(height)

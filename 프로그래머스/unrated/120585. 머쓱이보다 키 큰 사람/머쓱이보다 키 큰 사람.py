def solution(array, height):
    array.append(height)
    array.sort()
    array = array[::-1]
    return array.index(height)
def solution(arr):
    length = len(arr)
    if length & (length-1) != 0:
        zeros = abs(2**length.bit_length() - length)
        arr += [0] * zeros
    return arr

# 다른 풀이
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)


"""
2의 거듭제곱 확인 방법 O(1)로 해야 겨우 O(n)
logn으로 확인하면 그걸 n번 반복 -> o(nlogn)
길이 1000개 -> 가장 빠른방법은 각각 하드코딩하기 겨우 10개

"""

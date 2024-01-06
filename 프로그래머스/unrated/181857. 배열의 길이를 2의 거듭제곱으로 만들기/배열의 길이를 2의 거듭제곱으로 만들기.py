def solution(arr):
    length = len(arr)
    if length & (length-1) != 0:
        zeros = abs(2**length.bit_length() - length)
        arr += [0] * zeros
    return arr
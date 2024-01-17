def solution(s):
    integer = [int(i) for i in s.split()]
    return f'{min(integer)} {max(integer)}'
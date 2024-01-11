from collections import deque

def solution(s, n):
    answer = ''
    alphabet = [chr(c) for c in range(ord('a'),ord('z')+1)]*2
    for c in s:
        if c.isupper():
            answer += alphabet[alphabet.index(c.lower()) + n].upper()
        elif c == ' ':
            answer += ' '
        else:
            answer += alphabet[alphabet.index(c) + n]
    return answer
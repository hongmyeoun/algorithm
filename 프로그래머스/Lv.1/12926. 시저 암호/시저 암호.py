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

# 부등호로 확인하기
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer

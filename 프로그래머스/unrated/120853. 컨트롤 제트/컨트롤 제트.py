def solution(s):
    s = s.split()
    return sum(-int(s[i-1]) if s[i] == 'Z' else int(s[i]) for i in range(len(s)))
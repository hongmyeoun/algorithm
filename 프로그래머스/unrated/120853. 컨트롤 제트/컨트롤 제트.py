def solution(s):
    s = s.split()
    return sum(-int(s[i-1]) if s[i] == 'Z' else int(s[i]) for i in range(len(s)))

# pop()을 이용한 풀이
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)

def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
    return True

# 다른경우는 모드 false
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

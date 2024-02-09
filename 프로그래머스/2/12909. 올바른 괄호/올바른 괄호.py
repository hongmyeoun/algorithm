def solution(s):
    stack = []
    
    if s[0] == ")":
        return False
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif "(" in stack:
            stack.pop()
    
    return False if stack else True

# Try를 이용해서 pop()에러가 나면 False 
if c == ')':
    try:
        st.pop()
    except IndexError:
        return False

# 효율성 테스트 1,2 시간초과
# def solution(s):
#     while "()" in s:
#         s = s.replace("()","")
#         if s == "":
#             return True
        
#     return False

# 효율성 테스트 1,2 시간초과
# def solution(s):
#     for _ in range(len(s)//2):
#         s = s.replace("()","")
#     return True if s == "" else False


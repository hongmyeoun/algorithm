def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0

# s를 순회하면서
# 값을 stack에 저장
# stack이 비어있지 않고, stack 값과 순회중인 값이 같다면
# pop()
# 아니면 순회중인 값을 stack에 추가
# stack이 비어있다면 1, 아니면 0을 반환
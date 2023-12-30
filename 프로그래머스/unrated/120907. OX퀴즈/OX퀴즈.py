def solution(quiz):
    return ["O" if eval(eq.replace('=', '==')) else "X" for eq in quiz]
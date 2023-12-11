def solution(a, b):
    # answer = int(max(f'{a}{b}',f'{2 * a * b}'))
    a_str, b_str = str(a), str(b)
    answer = int(a_str + b_str) if int(a_str + b_str) > 2 * a * b else 2 * a * b
    return answer
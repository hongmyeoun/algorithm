def solution(n):
    return int(tri(n)[::-1], 3)

def tri(n):
    if n == 0:
        return '0'
    
    result = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        result = str(remainder) + result
    
    return result
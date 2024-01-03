def solution(n):
    count = 0
    for i in range(1,n+1):
        if is_composite(i):
            count += 1
    return count

def is_composite(n):
    return int(len([i for i in range(1,n+1) if not n%i]) >= 3)

def solution(slice, n):
    if n > slice:
        if n % slice == 0:
            return n//slice
        else:
            return n//slice + 1
    else:
        return 1

def solution(slice, n):
    return (n-1)//slice + 1

# divmod 사용
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)

int(m != 0) : int(true) -> 1반환 아니면 0반환

# def solution(slice, n):
#     if n > slice:
#         if n % slice == 0:
#             return n//slice
#         else:
#             return n//slice + 1
#     else:
#         return 1

def solution(slice, n):
    return (n-1)//slice + 1
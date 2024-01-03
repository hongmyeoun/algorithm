def solution(num, k):
    num = list(str(num))
    for i in range(len(num)):
        if num[i] == str(k):
            return i+1
    return -1

# try exception 활용
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1

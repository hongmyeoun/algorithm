def solution(arr):
    try:
        indexes = [index for index, value in enumerate(arr) if value == 2]
        
        return arr[min(indexes):max(indexes)+1]
    except ValueError:
        return [-1]
    except IndexError:
        return [-1]

# 효율적인 풀이
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

2가 없다면 [-1] 반환
아니면
arr.index(2)부터 arr의 길이 - 2가있는 마지막 인덱스

def solution(arr):
    try:
        indexes = [index for index, value in enumerate(arr) if value == 2]
        
        return arr[min(indexes):max(indexes)+1]
    except ValueError:
        return [-1]
    except IndexError:
        return [-1]
    
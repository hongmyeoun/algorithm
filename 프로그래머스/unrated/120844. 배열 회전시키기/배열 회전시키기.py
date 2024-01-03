def solution(numbers, direction):
    if direction == 'right':
        numbers[0], numbers[1:] = numbers[-1], numbers[0:-1]
    elif direction == 'left':
        numbers[-1], numbers[:-1] = numbers[0], numbers[1:]
    return numbers

# collection 라이브러리 사용
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        numbers[0], numbers[1:] = numbers[-1], numbers[0:-1]
    elif direction == 'left':
        numbers[-1], numbers[:-1] = numbers[0], numbers[1:]
    return numbers
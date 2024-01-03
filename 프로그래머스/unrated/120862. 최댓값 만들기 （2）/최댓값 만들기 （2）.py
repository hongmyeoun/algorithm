def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2] if numbers[-1] * numbers[-2] > numbers[0] * numbers[1] else numbers[0] * numbers[1]

# max() 사용
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 

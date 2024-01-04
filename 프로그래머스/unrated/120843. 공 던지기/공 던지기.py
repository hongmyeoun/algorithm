def solution(numbers, k):
    count = 0
    numbers = numbers * k
    for i in range(0,len(numbers),2):
        count += 1
        if k == count:
            return numbers[i]

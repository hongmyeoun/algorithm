# 의사코드
# 리스트의 인덱스 처음과 그다음을 비교 -> 마지막전과 마지막까지 반복
# 한번 반복하면 마지막 인덱스는 최대 or 최소값
# 그 값을 제외하고 다시 반복
# 기본값은 오름차순

example = [7,4,5,1,3]

def bubble_sort(numbers, reverse=False): # 기본값은 오름차순
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i): # 마지막 인덱스를 제외
            if not reverse:
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            else:
                if numbers[j] < numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(bubble_sort(example)) # [1, 3, 4, 5, 7]
print(bubble_sort(example, True)) # [7, 5, 4, 3, 1]
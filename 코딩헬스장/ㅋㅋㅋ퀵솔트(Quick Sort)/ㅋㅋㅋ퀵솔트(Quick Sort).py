# 의사코드(오름차순)
    # 피벗은 리스트의 중간에 있는 값
    # 리스트의 양쪽의 인덱스에서 피벗과 값을 비교
    # 왼쪽부터 증가하는 인덱스는 그 값이 피벗보다 클때 증가를 멈춤
    # 오른쪽부터 감소하는 인덱스는 그 값이 피벗보다 작을때 증가를 멈춤
    # 둘 다 멈췄을때 둘의 값을 바꿈
    # 그리고 인덱스를 증가, 감소 시킴
    # 왼쪽부터 증가하는 인덱스가 오른쪽부터 시작하는 인덱스와 같아지거나 작아지면 반복 종료
    # 피벗 기준 왼쪽과 오른쪽을 나누어 이 과정을 반복
    # 리스트 길이가 1과 작거나 같으면 그 값을 반환

def quick_sort(numbers, reverse=False):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[len(numbers)//2]

    start = 0
    end = len(numbers) - 1

    while start <= end:

        if not reverse:
            while numbers[start] < pivot: 
                start += 1
            while numbers[end] > pivot:
                end -= 1
        else:
            while numbers[start] > pivot: 
                start += 1
            while numbers[end] < pivot:
                end -= 1

        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1 
        end -= 1 

    left = numbers[:start-1] # 슬라이싱으로 값을 처리 -> 매번 새로운 리스트를 생성하고 할당
    right = numbers[start:] # 그로인해 quick_sort2보다 느림

    return quick_sort(left, reverse) + [pivot] + quick_sort(right, reverse)

# 의사코드
    # 피벗은 리스트에 중간에 있는 값
    # 리스트를 순회하면서, 피벗보다 작으면 left 리스트에 추가
    # 크면 right 리스트에 추가
    # 이과정을 리스트이 길이가 1이하가 될때까지 반복
def quick_sort2(numbers, reverse=False):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers)//2] 
    left, right = [], []

    for i in numbers:
        if not reverse:
            if i < pivot:
                left.append(i) # 기존에 있는 리스트에 추가하는 방식
            elif i > pivot:
                right.append(i) # quick_sort보다는 메모리 사용량을 줄인 효율적방식
        else:
            if i > pivot:
                left.append(i)
            elif i < pivot:
                right.append(i)

    return quick_sort2(left, reverse) + [pivot] + quick_sort2(right, reverse)


print(quick_sort([5,1,6,4,3,2,7])) # [1, 2, 3, 4, 5, 6, 7]
print(quick_sort([5,1,6,4,3,2,7], True)) # [7, 6, 5, 4, 3, 2, 1]
print(quick_sort2([5,1,6,4,3,2,7])) # [1, 2, 3, 4, 5, 6, 7]
print(quick_sort2([5,1,6,4,3,2,7], True)) # [7, 6, 5, 4, 3, 2, 1]

# 어떤분 코드 참조 테스트
import time
import random

def test_sort_functions():
    arr = [random.randint(0, 1000) for _ in range(10000)]

    start = time.time()
    quick_sort(arr.copy())  # quick_sort 함수 테스트
    end = time.time()
    print(f"quick_sort took {end - start} seconds.")

    start = time.time()
    quick_sort2(arr.copy())  # quick_sort2 함수 테스트
    end = time.time()
    print(f"quick_sort2 took {end - start} seconds.")

    start = time.time()
    arr.sort()  # 파이썬 내장 정렬 함수 테스트
    end = time.time()
    print(f"Team sort took {end - start} seconds.")

test_sort_functions()

# Result
# quick_sort took 0.021941423416137695 seconds.
# quick_sort2 took 0.010970354080200195 seconds.
# Team sort took 0.0009975433349609375 seconds.

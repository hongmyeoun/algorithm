def findSecond(numbers):
    first = findFirst(numbers)
    while numbers.count(first):
        numbers.pop(numbers.index(first))
    return findFirst(numbers)

def findFirst(numbers):
    first = numbers[0]

    for i in numbers:
        if i > first:
            first = i

    return first

# 처음 코드
# 가장 큰 수 다음수가 두번째로 큰 수
# 배열에서 가장 큰 수를 한번 제거한 후
# 가장 큰 수를 찾기
# -> findFirst에서 시간 복잡도가 O(n)인데, findSecond에서 findFirst를 호출하고 리스트를 순회하기 때문에 시간복잡도 O(n^2)

def findSecond2(numbers):

    first = numbers[0]
    second = numbers[0]

    for i in numbers[1:]:
        if i > first:
            second = first
            first = i
        elif i < first and i > second:
            second = i

    return second

# 배열의 첫번째 값을 가장 큰수와 두번째로 큰 수로 두고
# 배열의 두번째값부터 순회하면서
# 해당 값이 가장 큰 수 보다 크면 
# 그 값이 가장 큰 수가 됨
# 가장 큰 수는 두번째 큰 수가 됨
# 가장 큰수보다 작고, 두번째 큰 수보다 크면
# 두번째 큰 수가 됨
# => 시간복잡도 O(n)

def findSecond3(numbers):
    return list(set(numbers))[-2]

# numbers = list(set(numbers)) 
# -> 이렇게 중복제거하려 했는데, 바로 정렬됨
# => Python 3.6이상에선 set을 썼을때 정렬된다고 함
# 이걸 이용함
# 시간 복잡도 O(nlogn)

import time
import random

def test_sort_functions():
    arr = [random.randint(0, 1000) for _ in range(100000)]

    start = time.time()
    findSecond(arr.copy())
    end = time.time()
    print(f"findSecond : O(n^2) {end - start} seconds.")

    start = time.time()
    findSecond2(arr.copy())
    end = time.time()
    print(f"findSecond2 : O(n) {end - start} seconds.")

    start = time.time()
    findSecond3(arr.copy())
    end = time.time()
    print(f"findSecond3 : O(nlogn) {end - start} seconds.")

test_sort_functions()
# findSecond : O(n^2) 0.1406252384185791 seconds.
# findSecond2 : O(n) 0.006981372833251953 seconds.
# findSecond3 : O(nlogn) 0.002991914749145508 seconds.

print(findSecond([5,1,57,52,57,57,13,53,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57])) # 53
print(findSecond2([5,1,57,52,57,57,13,53,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57])) # 53
print(findSecond3([5,1,57,52,57,57,13,53,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57])) # 53

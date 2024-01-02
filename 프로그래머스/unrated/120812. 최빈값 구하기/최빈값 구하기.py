def solution(array):
    set_array = list(set(array))
    num_count = [array.count(i) for i in set_array]
    answer = -1
    
    if num_count.count(max(num_count)) == 1:
        answer = set_array[num_count.index(max(num_count))]
        
    return answer

# 의사코드
    # count로 세면될듯?
    # 주사위랑 동일하게 맞춰놓고 최빈값이랑 최빈값 출현 횟수랑 다르면 -1 return
    # 실패
	# array = [1, 1, 1, 1, 2, 3, 3, 4]
	# num_count = [4, 4, 4, 4, 1, 2, 2, 1]
	# num_count.count(num_count) = [4, 4, 4, 4, 2, 2, 2, 2]
	# array = [1, 1, 1, 1, 2, 3, 3, 4, 3, 3]
	# num_count = [4, 4, 4, 4, 1, 4, 4, 1, 4, 4]
	# num_count.count(num_count) = [8, 8, 8, 8, 2 ,8, 8, 2, 8, 8]
	# max(num_count) != max([num_count.count(i) for i in num_count]) -> -1
	# 아니면 array[num_count.index(max(num_count))]
    
    # max([num_count.count(i) for i in num_count]) 1,1,1,1,1이 많아질때 문제가 생김
    # array를 set으로 받음
    # 그런후 array를 카운트
    # 최빈값을 세서 1개면 그값을 출력
    # 아니면 -1출력

# collections 라이브러리 사용
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]

from collections import Counter: collections 모듈에서 Counter 클래스를 가져옵니다. Counter 클래스는 주어진 iterable(리스트, 문자열 등)의 요소들의 개수를 세는 데 사용됩니다.

a = Counter(array).most_common(2): 입력 리스트 array의 각 요소의 빈도를 세고, 빈도가 높은 순으로 상위 2개의 요소를 튜플의 리스트로 반환합니다. 이 리스트를 변수 a에 저장합니다.

if len(a) == 1:: 만약 a의 길이가 1이라면, 입력 리스트에 중복된 요소가 없는 경우입니다. 그 경우에는 리스트의 첫 번째 요소를 반환합니다.

if a[0][1] == a[1][1]:: 두 번째로 높은 빈도의 요소와 가장 높은 빈도의 요소가 동일한 경우, 즉 동률인 경우에는 -1을 반환합니다.

return a[0][0]: 그 외의 경우에는 빈도가 가장 높은 요소를 반환합니다.

이 함수는 리스트에서 가장 빈도가 높은 요소를 찾아 반환하며, 동률이 있을 경우에는 -1을 반환합니다.

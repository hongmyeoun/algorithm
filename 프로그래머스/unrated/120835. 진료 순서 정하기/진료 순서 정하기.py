def solution(emergency):
    em_dict = dict(zip(sorted(emergency, reverse=True), list(range(1,len(emergency)+1))))
    return [em_dict[i] for i in emergency]

# index로 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

인덱스 쓰면 O(N**2)

시간 복잡도 비교

dictionary 풀이
sorted(emergency, reverse=True): emergency 리스트를 내림차순으로 정렬합니다. 이 부분의 시간 복잡도는 O(N log N), 여기서 N은 emergency 리스트의 길이입니다.
zip(sorted(emergency, reverse=True), list(range(1,len(emergency)+1))): 정렬된 리스트와 해당 인덱스를 튜플로 묶습니다. 이 부분의 시간 복잡도는 O(N).
em_dict = dict(...): 튜플로 묶은 값을 딕셔너리로 변환합니다. 이 부분의 시간 복잡도도 O(N).
[em_dict[i] for i in emergency]: emergency의 각 원소에 대해 딕셔너리에서 값을 가져와 새로운 리스트를 만듭니다. 이 부분의 시간 복잡도는 O(N).

따라서 전체 코드의 시간 복잡도는 O(N log N) + O(N) + O(N) + O(N) = O(N log N)입니다.

index 풀이
sorted(emergency, reverse=True): emergency 리스트를 내림차순으로 정렬합니다. 이 부분의 시간 복잡도는 O(N log N).
[sorted(emergency, reverse=True).index(e) + 1 for e in emergency]: emergency의 각 원소에 대해 정렬된 리스트에서 해당 원소의 인덱스를 찾아와서 1을 더합니다. 
이 부분의 시간 복잡도는 O(N^2)입니다. 왜냐하면 리스트에서 특정 원소의 인덱스를 찾는 index() 메소드는 최악의 경우에 O(N)의 시간이 걸리기 때문입니다.

따라서 전체 코드의 시간 복잡도는 O(N log N) + O(N^2) = O(N^2)입니다.

결론
두 코드 중에서 dictionary가 두 배 정도 더 효율적인 시간 복잡도를 가지고 있습니다.

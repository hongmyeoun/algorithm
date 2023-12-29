def solution(numlist, n):
    # 각 숫자에서 n을 뺀 값의 절대값 리스트 생성
    length = [abs(i - n) for i in numlist]
    
    # 인덱스와 원래 숫자를 튜플로 묶은 리스트 생성
    indexed_numlist = list(zip(length, numlist))
    
    # 절대값에 따라 정렬, 길이가 같으면 numlist의 값이 큰 것이 먼저 올 수 있도록 정렬
    indexed_numlist.sort(key=lambda x: (x[0], -x[1]))   
    
    return [x[1] for x in indexed_numlist]

# 도저히 못풀겠어서 수도코드를 짜놓고 gpt에게 답을 부탁함
    # length = [abs(i - n) for i in numlist]
    # numlist에 모든 숫자에서 n을 뺌
    # 그 뺀값을 새로운 list로 만듦
    # 절대값으로 만들어
    # [1,2,3,4,5,6]
    # [3,2,1,0,1,2]
    # 그 리스트를 정렬
    # [0,1,1,2,2,3]
    # 그걸 numlist의 숫자와 매칭
    # 만약 length값이 같다면, 더 큰 numlist값이 빠른 인덱스

list(zip(length, numlist))를 통해 length와 numlist를 묶음
이를 정렬하는데,
list.sort(key=lambda x: (x[0], -x[1]))
key에 lambda식에 x는 .sort()앞의 list
x의 0번째 요소는 양수(오름차순)으로 정렬
x의 1번째 요소는 음수(내림차순)으로 정렬
(x[0], -x[1])를 통해 값을 tuple로 반환

# sorted()를 사용할때 key를 사용해 정렬을 한 식
def solution(numlist, n):
    return sorted(numlist, key = lambda x: [abs(x-n),-x])

여기서 lambda식의 x는 numlist가 된다.
즉 거리는 오름차순, 숫자는 내림차순으로 정렬한뒤 [](list)로 반환

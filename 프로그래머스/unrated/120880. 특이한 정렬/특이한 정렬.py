def solution(numlist, n):
    # 각 숫자에서 n을 뺀 값의 절대값 리스트 생성
    length = [abs(i - n) for i in numlist]
    
    # 인덱스와 원래 숫자를 튜플로 묶은 리스트 생성
    indexed_numlist = list(zip(length, numlist))
    
    # 절대값에 따라 정렬, 길이가 같으면 numlist의 값이 큰 것이 먼저 올 수 있도록 정렬
    indexed_numlist.sort(key=lambda x: (x[0], -x[1]))    
    
    # 정렬된 리스트에서 숫자만 추출하여 반환
    answer = [x[1] for x in indexed_numlist]
    return answer

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
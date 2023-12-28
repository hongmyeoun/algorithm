def solution(arr, query):
    for idx, i in enumerate(query):
        arr = arr[:i+1] if not idx % 2 else arr[i:]
    return arr
    
# 처음 제출 코드 (실패)
def solution(arr, query):
    for i in query:
        arr = arr[:i+1] if i % 2 == 0 else arr[i:]
    return arr

실패 이유
query의 index를 2로 나눴을때 query의 요소로 슬라이싱 해야함.
하지만 index를 사용하지 않음

그래서 수정함

# 두번째 통과 코드
def solution(arr, query):
    for i in range(len(query)):
        if len(arr) > query[i]:
            if i % 2 == 0:
                arr = arr[:query[i]+1]
            else:
                arr = arr[query[i]:]
    return arr

query의 index의 홀짝을 판별한 후, query 요소로 슬라이싱하는 로직으로 변경.
arr가 더 짧을경우 실행이 안될까 라고 생각해 조건문을 붙였음.

def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

조건문 필요없없음

# index와 요소를 다 사용하는 것이기 때문에 enumerate()사용
def solution(arr, query):
    for idx, i in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    return arr

# 조건문 간소화
def solution(arr, query):
    for idx, i in enumerate(query):
        arr = arr[:i+1] if not idx % 2 else arr[i:]
    return arr

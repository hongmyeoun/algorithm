def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                result = 1
            else:
                return 0
    return result

# symmetric matrix의 성질
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))

이 코드는 2차원 리스트 arr을 받아서 해당 리스트가 행렬 전치(transpose) 결과와 동일한지 여부를 판단하는 함수입니다.

zip(*arr): arr의 행과 열을 바꾸어 튜플의 리스트를 생성합니다. 이는 행렬을 전치하는 것과 같습니다.
map(list, ...): 각 튜플을 리스트로 변환합니다.
list(...): 전치된 행렬을 리스트로 변환합니다.
arr == ...: 원래의 리스트와 전치된 리스트를 비교합니다.
int(...): 비교 결과를 정수로 변환합니다. (True는 1로, False는 0으로 변환됩니다.)
따라서 solution 함수는 원래의 행렬과 그것의 전치가 같은지를 판단하고, 결과를 1 또는 0으로 반환합니다. 이는 불리언(True 또는 False) 값을 정수로 변환하는 방식으로 결과를 표현하고 있습니다.

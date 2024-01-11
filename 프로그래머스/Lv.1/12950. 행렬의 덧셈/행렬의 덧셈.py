def solution(arr1, arr2):
    return [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]


# zip으로 더 간단히
def sumMatrix(A,B):
    return [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]

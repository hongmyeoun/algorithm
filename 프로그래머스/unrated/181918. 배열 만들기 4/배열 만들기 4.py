def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    return stk

# stk가 없거나 마지막자리가 작으면 이조건만 다르고 실행은 같음
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        a = arr[i]
        if len(stk)==0 or stk[-1] < a: 
            stk.append(a)
            i += 1
        else:
            stk.pop()
    return stk

# 반복문이 두개이긴함
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk

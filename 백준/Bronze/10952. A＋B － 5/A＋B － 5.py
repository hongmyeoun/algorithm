sumList = []
while (True):
    A, B = map(int, input().split())
    if A + B == 0:
        break
    sumList.append(A + B)
for i in sumList:
    print(i)
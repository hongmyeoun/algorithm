import sys
T = int(sys.stdin.readline())
sumList = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sumList.append(A+B)

for i in sumList:
    print(i)

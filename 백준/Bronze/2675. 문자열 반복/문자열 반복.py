T = int(input())

IList = []
SList = []
for _ in range(T):
    I, S = input().split()
    IList.append(int(I))
    SList.append(S)

for i in range(T):
    S = [j for j in SList]
    for k in S[i]:
        print(k*IList[i], end="")
    print("",end=" ")

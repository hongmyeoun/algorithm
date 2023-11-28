total = int(input())
variables = int(input())
sumList = []
for _ in range(variables):
    price, amount = map(int, input().split())
    total_price = price * amount
    sumList.append(total_price)
    # print(sumList)
# print(sum(sumList))
if total == sum(sumList):
    print("Yes")
else:
    print("No")
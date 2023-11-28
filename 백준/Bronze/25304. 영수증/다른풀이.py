total = int(input())
variables = int(input())
total_price = 0

for _ in range(variables):
    price, amount = map(int, input().split())
    total_price += price * amount

print("Yes" if total == total_price else "No")

N = int(input())
number = input()
if len(number) == N:
    number_list = [int(i) for i in number]
print(sum(number_list))

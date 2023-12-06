student = 30

student_numList = list(range(1, student+1))

while True:
    A = int(input())
    student_numList.remove(A)
    if len(student_numList) < 3:
        break

print(min(student_numList))
print(max(student_numList))
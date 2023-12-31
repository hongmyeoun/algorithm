solution = lambda n: sorted([i for i in range(1, n+1) if not n % i])

# 의사코드
  1부터 n까지 n을 나눴을때 나머지가 0이 되는 수를 append

# 리스트컴프리헨션 문법(?) else가 꼭 있어야 하는줄 알았음... else None 이거하다가 알아냄

[표현식 for 항목 in iterable if 조건]
표현식 (Expression): 리스트에 추가될 값에 대한 표현식
항목 (Item): iterable에서 가져온 각 항목에 대한 변수명
iterable: 반복 가능한 객체 (리스트, 튜플, 문자열 등)
조건 (Condition): 선택적으로 추가할 값에 대한 조건

else 구문은 리스트 컴프리헨션에서 직접 사용되지 않음,
if-else 표현식을 사용하여 값을 조건에 따라 선택적으로 생성할 수 있음
[값_if_true if 조건 else 값_if_false for 항목 in iterable]

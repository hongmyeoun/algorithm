T = int(input()) # 테스트 케이스의 개수 T를 입력받는다.
ans = [] # 정답을 저장할 리스트를 만든다.
for _ in range(T): # T만큼 반복한다.
    A, B = map(int, input().split()) # A와 B를 입력받는다.
    ans.append(A+B) # A와 B를 더한 값을 정답 리스트에 추가한다.

for i in ans: # 정답 리스트를 반복한다.
    print(i) # 정답 리스트의 요소를 출력한다.
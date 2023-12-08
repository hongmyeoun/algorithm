alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S = input().lower() # abcd
SList = [i for i in S] # [a, b, c, d]

# SList에 있는 요소가 alphabet에 있다면 
for a_idx, a in enumerate(alphabet): # 0 a
    for s_idx, s in enumerate(SList): # 0 a
        if s == a: # a == a 
            alphabet[a_idx] = s_idx # alphabet[0] = 0
            break
        elif isinstance(a, str):
            alphabet[a_idx] = -1

for i in alphabet:
    print(i, end=' ')
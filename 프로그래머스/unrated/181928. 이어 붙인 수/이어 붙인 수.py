def solution(num_list):
    odd = ''
    even = ''
    for i in num_list:
        if i % 2 == 1:
            odd += str(i)
        else:
            even += str(i)
    
    return int(odd) + int(even)


# join을 쓰는 방법 기억하자

def solution(num_list):
    even=int(''.join([str(i) for i in num_list if i%2==0]))
    odd=int(''.join([str(i) for i in num_list if not i%2==0]))
    return even+odd

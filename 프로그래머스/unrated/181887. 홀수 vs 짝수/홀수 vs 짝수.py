def solution(num_list):
    odd_sum = 0
    even_sum = 0
    
    for idx, i in enumerate(num_list):
        if idx % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
            
    if odd_sum > even_sum:
        return odd_sum
    elif odd_sum == even_sum:
        return odd_sum
    else:
        return even_sum

# 인덱싱으로 풀이
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

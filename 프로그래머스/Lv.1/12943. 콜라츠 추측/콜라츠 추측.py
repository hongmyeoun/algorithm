def solution(num):
    count = 0
    
    while True:
        if num == 1:
            break
        if count == 500:
            return -1
        
        if not num%2:
            num //= 2
        else:
            num = num*3 + 1
        
        count += 1
    return count
def solution(num, total):
    answer = []
    end = int((((total * 2) / num) + num - 1) / 2)
    while num > 0:
        answer.append(end)
        end -= 1
        num -= 1
    answer.sort()
    return answer

# m == (((total * 2) / n) + n - 1) / 2

# hint

1부터 m까지의 자연수의 합을 구하는공식은 아래와 같습니다.
(n * (n + 1)) / 2 == total

자 그렇다면 도출해내야하는 리스트의 마지막 원소가 m일텐데 위 공식을 이용하여 아래와 같이 도출해낼수있습니다.
m == (((total * 2) / n) + n - 1) / 2

# 다른 풀이
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

1. result를 일반화 시키면 
[x+0, x+1, x+2, x+3 ... x + (num-1)]

2. 그리고 위 값을 전부 더한 값이 total이 됨. 
total = num*x + num*(num-1)//2
※ result의 전체요소의 갯수는 num개 이므로 x의 갯수는 num개 이고 상수 부분은 첫번째 항이 0이고 마지막항이 num-1인 등차가 1인 등차수열의 합임.

3. 2번에서 도출한 공식을 이제 위 코드에 대입해보면 
[(total - (num * (num - 1) // 2)) // num + i for i in range(num)] = [num*x + (num * (num - 1) // 2)) - (num * (num - 1) // 2)) // num + i for i in range(num)] = [num*x // num + i for i in range(num)] = [x + i for i in range(num)] 
1번에서의 result x식과 일치하므로 정답이 됨.

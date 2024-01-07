def solution(common):
    if is_arithmetic(common):
        return 2*common[-1] - common[-2]
    elif is_geometric(common):
        return common[-1]**2/common[-2]

def is_arithmetic(arr):
    differences = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return all(diff == differences[0] for diff in differences)

def is_geometric(arr):
    ratios = [arr[i+1]/arr[i] for i in range(len(arr)-1)]
    return all(ratio == ratios[0] for ratio in ratios)

# 함수 안나누고 간단하게 하는 방법
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer

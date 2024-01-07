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
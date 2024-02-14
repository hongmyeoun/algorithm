from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights.reverse()
    time = 0
    bridge_weight = 0
    
    while bridge:
        time += 1
        bridge_weight -= bridge.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[-1] <= weight:
                truck = truck_weights.pop()
                bridge_weight += truck
                bridge.append(truck)
            else:
                bridge.append(0)
    
    return time

# 모든 트럭이 지나면 최소 몇초?
# 다리엔 트릭이 최대 bridge_length대 올라갈 수 있음
# 다리는 weight 이하까지 무게를 견딤
# 다리에 완전히 오르지 않은 트럭은 무시
# bridge_length대 = 2, weight = 8, truck_weights = [7,4,5,6]
# 0 [7,4,5,6] [00] []
# 1 [4,5,6] [07] []
# 2 [4,5,6] [70] []
# 3 [5,6] [04] [7]
# 4 [6] [45] [7]
# 5 [6] [50] [7,4]
# 6 [] [06] [7,4,5]
# 7 [] [60] [7,4,5]
# 8 [] [00] [7,4,5]
# 8sec

# 비슷한 풀이 순서랑 조건문만 바뀜(프로그래머스)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

# under 0.1sec
from collections import deque

def solution(bridge_length, weight, truck_weights):
    b, w, t = bridge_length, weight, truck_weights
    time = deque([1])
    wsum = deque([t[0]])
    sec = 0
    for v, i in enumerate(t[1:]):
        if i <= weight - sum(wsum):
                time.append(1)
                wsum.append(i)
                if sum(time) - time[0] == b:
                    sec += time.popleft()
                    wsum.popleft()
                continue
        if i <= weight - sum(wsum) + wsum[0]:
            sec += time.popleft()
            wsum.popleft()
            time.append(b - sum(time))
            wsum.append(i)
            continue
        while i > weight - sum(wsum):
            sec += time.popleft()
            wsum.popleft()
        time.append(b - sum(time))
        wsum.append(i)
    for i in time:
        sec += i
    return sec + b

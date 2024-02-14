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
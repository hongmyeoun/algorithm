def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer

# 두줄 코드
def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k)

리스트 컴프리헨션으로 더하면됨, 왜 나는 테스트할때 result = []로 만들어놓고 sum할 생각을 안했을까?

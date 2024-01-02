def solution(todo_list, finished):
    return [todo_list[idx] for idx, i in enumerate(finished) if not i]
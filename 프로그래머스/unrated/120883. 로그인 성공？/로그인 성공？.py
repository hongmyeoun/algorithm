def solution(id_pw, db):
    answer = ''
    input_id = id_pw[0]
    input_pw = id_pw[1]
    for idx, db_id_pw in enumerate(db):
        user_id, user_pw = db_id_pw
        if input_id == user_id and input_pw == user_pw:
            answer = 'login'
            break
        if input_id == user_id and input_pw != user_pw:
            answer = 'wrong pw'
            break
        if input_id != user_id:
            answer = 'fail'
    return answer
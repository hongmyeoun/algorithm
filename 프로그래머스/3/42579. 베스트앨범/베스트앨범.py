def solution(genres, plays):
    answer = []
    song_dict = {}
    
    for idx, genre in enumerate(genres):
        if genre not in song_dict:
            song_dict[genre] = []
        song_dict[genre].append((idx, plays[idx]))

    genre_play_sum = [(genre, sum(play for _, play in songs)) for genre, songs in song_dict.items()]
    genre_play_sum.sort(key=lambda x: x[1], reverse=True)

    for genre, _ in genre_play_sum:
        songs = song_dict[genre]
        songs.sort(key=lambda x: (-x[1], x[0]))
        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])

    return answer

# dict에 장르를 key, 인덱스와 재생수인 plays는 value값으로 저장
# 만약 장르가 없으면 []로 생성
# (idx, plays[idx])를 append
# 장르별 플레이 횟수의 합을 구함
# 장르별 플레이 횟수를 내림차순으로 정렬
# 장르별 플레이 횟수의 장르를 순회
# dict에 value값을 내림차순으로 정렬
# 정렬된 value값중 최대 두개까지 answer에 append
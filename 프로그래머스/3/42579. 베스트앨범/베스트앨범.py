def solution(genres, plays):
    answer = []
    total_plays = {}
    song_genres = {}
    
    # for 문 i에 해당하는 데이터 처리
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        # 총 재생 수 순으로 정렬
        if genre not in total_plays:
            total_plays[genre] = play
        else:
            total_plays[genre] += play
        
        # 장르 별로 노래 모음
        if genre not in song_genres:
            song_genres[genre] = [(play, i)]
        else:
            song_genres[genre].append((play, i))
            
    # 조회수 순으로 정렬
    total_plays = sorted(total_plays.items(), key=lambda x : -x[1])
    
    for genre, _ in total_plays:
        songs = sorted(song_genres[genre], key=lambda x : (-x[0], x[1]))
        print(songs)
        count = 0
        for song in songs:
            if count >= 2:
                break
            answer.append(song[1])
            count += 1
            
    return answer
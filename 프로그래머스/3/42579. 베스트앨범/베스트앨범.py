from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(list)
    plays_dict = defaultdict(int)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genres_dict[genre].append((i, play))
        plays_dict[genre] += play
    
    sorted_plays_dict = sorted(plays_dict.items(), key=lambda x : -x[1])
    
    for genre, _ in sorted_plays_dict:
        sorted_genres_dict = sorted(genres_dict[genre], key=lambda x:(-x[1], x[0]))
        
        count = 0
        for k in sorted_genres_dict:
            if count >= 2:
                break
            answer.append(k[0])
            count += 1
    return answer

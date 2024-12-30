def solution(participant, completion):
    participant_dict = {}
    
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1
    
    for name in completion:
        participant_dict[name] -= 1
        
    for name in participant_dict:
        if participant_dict[name] == 1:
            return name
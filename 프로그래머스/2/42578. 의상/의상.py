from collections import defaultdict

def solution(clothes):

    clothes_dict = defaultdict(list)
    
    for i in range(len(clothes)):
        category = clothes[i][1]
        name = clothes[i][0]
        clothes_dict[category].append(name)
    
    answer = 1
    for category in clothes_dict:
        answer *= (len(clothes_dict[category]) + 1)
    
    return answer - 1
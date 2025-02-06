from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)
    distance[1] = 0
    
    q = deque()
    q.append(1)
    
    while q:
        n = q.popleft()
    
        for i in graph[n]:
            if distance[i] == -1:
                distance[i] = distance[n] + 1
                q.append(i)
                
    max_distance = max(distance)
    
    answer = distance.count(max_distance)
        
    return answer
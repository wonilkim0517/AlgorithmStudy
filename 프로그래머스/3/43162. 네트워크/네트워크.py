from collections import deque

def bfs(v, visited, n, computers):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            bfs(i, visited, n, computers)
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, n, computers)
            answer += 1
            
    return answer
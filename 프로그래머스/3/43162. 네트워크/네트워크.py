def dfs(v, visited, computers, n):
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(i, visited, computers, n)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers, n)
            answer += 1
            
    return answer
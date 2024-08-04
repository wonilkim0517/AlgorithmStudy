import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    global cnt
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            cnt +=1
            dfs(i)

dfs(1)
print(cnt)
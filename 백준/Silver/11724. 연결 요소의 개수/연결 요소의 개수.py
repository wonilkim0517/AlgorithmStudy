import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
        
print(cnt)

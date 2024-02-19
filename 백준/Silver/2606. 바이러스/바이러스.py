import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

network = {}
visited = [False for _ in range(N + 1)]
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    if u in network:
        network[u].append(v)
    else:
        network[u] = [v]

    if v in network:
        network[v].append(u)
    else:
        network[v] = [u]

def dfs(u):
    visited[u] = True
    if u in network:
        for v in network[u]:
            if visited[v] == False:
                dfs(v)

dfs(u=1)

for u in range(2, N + 1):
    if visited[u]:
        count += 1
        
print(count)
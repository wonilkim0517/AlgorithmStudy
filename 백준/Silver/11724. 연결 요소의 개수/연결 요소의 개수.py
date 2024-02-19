import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(neighbour for neighbour in graph[current] if not visited[neighbour])

for u in range(1, N + 1):
    if not visited[u]:
        dfs(u)
        count += 1

print(count)

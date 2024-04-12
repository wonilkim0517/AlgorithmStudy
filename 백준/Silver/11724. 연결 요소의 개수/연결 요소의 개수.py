import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(start):
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)


def count_connected_components():
    count = 0
    for u in range(1, N + 1):
        if not visited[u]:
            dfs(u)
            count += 1
    return count


N, M = map(int, input().split())

graph = defaultdict(list)
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = count_connected_components()
print(result)

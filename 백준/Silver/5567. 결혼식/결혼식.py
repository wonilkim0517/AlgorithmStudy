import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = visited[current] + 1


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
result = 0
for i in range(2, n + 1):
    if 1 <= visited[i] <= 3:
        result += 1

print(result)
